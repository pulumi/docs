---
title: Module rds
---

<a href="../index.html">@pulumi/aws</a> &gt; rds

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ClusterInstance">class ClusterInstance</a>
* <a href="#ClusterParameterGroup">class ClusterParameterGroup</a>
* <a href="#ClusterSnapshot">class ClusterSnapshot</a>
* <a href="#EventSubscription">class EventSubscription</a>
* <a href="#Instance">class Instance</a>
* <a href="#OptionGroup">class OptionGroup</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#SecurityGroup">class SecurityGroup</a>
* <a href="#Snapshot">class Snapshot</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getClusterSnapshot">function getClusterSnapshot</a>
* <a href="#getEventCategories">function getEventCategories</a>
* <a href="#getInstance">function getInstance</a>
* <a href="#getSnapshot">function getSnapshot</a>
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
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetClusterSnapshotArgs">interface GetClusterSnapshotArgs</a>
* <a href="#GetClusterSnapshotResult">interface GetClusterSnapshotResult</a>
* <a href="#GetEventCategoriesArgs">interface GetEventCategoriesArgs</a>
* <a href="#GetEventCategoriesResult">interface GetEventCategoriesResult</a>
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

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts">rds/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts">rds/clusterInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts">rds/clusterParameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts">rds/clusterSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts">rds/eventSubscription.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts">rds/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts">rds/getClusterSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts">rds/getEventCategories.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts">rds/getInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts">rds/getSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts">rds/instance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts">rds/optionGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts">rds/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts">rds/securityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts">rds/snapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts">rds/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L30">class Cluster</a>
</h2>

Manages a [RDS Aurora Cluster][2]. To manage cluster instances that inherit configuration from the cluster (when not running the cluster in `serverless` engine mode), see the [`aws_rds_cluster_instance` resource](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html). To manage non-Aurora databases (e.g. MySQL, PostgreSQL, SQL Server, etc.), see the [`aws_db_instance` resource](https://www.terraform.io/docs/providers/aws/r/db_instance.html).

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
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L201">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L39">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L48">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L52">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L57">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L61">property backtrackWindow</a>
</h3>

```typescript
public backtrackWindow: pulumi.Output<number | undefined>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L65">property backupRetentionPeriod</a>
</h3>

```typescript
public backupRetentionPeriod: pulumi.Output<number | undefined>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L69">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L73">property clusterIdentifierPrefix</a>
</h3>

```typescript
public clusterIdentifierPrefix: pulumi.Output<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L77">property clusterMembers</a>
</h3>

```typescript
public clusterMembers: pulumi.Output<string[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L81">property clusterResourceId</a>
</h3>

```typescript
public clusterResourceId: pulumi.Output<string>;
```


The RDS Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L85">property databaseName</a>
</h3>

```typescript
public databaseName: pulumi.Output<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L89">property dbClusterParameterGroupName</a>
</h3>

```typescript
public dbClusterParameterGroupName: pulumi.Output<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L93">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L97">property deletionProtection</a>
</h3>

```typescript
public deletionProtection: pulumi.Output<boolean | undefined>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L114">property engineMode</a>
</h3>

```typescript
public engineMode: pulumi.Output<string | undefined>;
```


The database engine mode. Valid values: `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L118">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The database engine version. Updating this argument results in an outage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L124">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L128">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L132">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
public iamDatabaseAuthenticationEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation][6] for availability and limitations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L136">property iamRoles</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L140">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L145">property masterPassword</a>
</h3>

```typescript
public masterPassword: pulumi.Output<string | undefined>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L149">property masterUsername</a>
</h3>

```typescript
public masterUsername: pulumi.Output<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L153">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L158">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L162">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L167">property readerEndpoint</a>
</h3>

```typescript
public readerEndpoint: pulumi.Output<string>;
```


A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L171">property replicationSourceIdentifier</a>
</h3>

```typescript
public replicationSourceIdentifier: pulumi.Output<string | undefined>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L172">property s3Import</a>
</h3>

```typescript
public s3Import: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L176">property scalingConfiguration</a>
</h3>

```typescript
public scalingConfiguration: pulumi.Output<{ ... } | undefined>;
```


Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L180">property skipFinalSnapshot</a>
</h3>

```typescript
public skipFinalSnapshot: pulumi.Output<boolean | undefined>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L184">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L188">property sourceRegion</a>
</h3>

```typescript
public sourceRegion: pulumi.Output<string | undefined>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L192">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L196">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L201">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L25">class ClusterInstance</a>
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

~> **NOTE:** Deletion Protection from the RDS service can only be enabled at the cluster level, not for individual cluster instances. You can still add the [`prevent_destroy` lifecycle behavior](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy) to your Terraform resource configuration if you desire protection from accidental deletion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L170">constructor</a>
</h3>

```typescript
new ClusterInstance(name: string, args: ClusterInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L34">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L42">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L46">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of cluster instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L50">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L54">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L58">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The identifier of the [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L62">property dbParameterGroupName</a>
</h3>

```typescript
public dbParameterGroupName: pulumi.Output<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L66">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L70">property dbiResourceId</a>
</h3>

```typescript
public dbiResourceId: pulumi.Output<string>;
```


The region-unique, immutable identifier for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L74">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The DNS address for this instance. May not be writable

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L81">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L85">property engineVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L89">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L93">property identifierPrefix</a>
</h3>

```typescript
public identifierPrefix: pulumi.Output<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L112">property instanceClass</a>
</h3>

```typescript
public instanceClass: pulumi.Output<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes. Please see [AWS Documentation][7] for complete details.
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L116">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key if one is set to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L120">property monitoringInterval</a>
</h3>

```typescript
public monitoringInterval: pulumi.Output<number | undefined>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L126">property monitoringRoleArn</a>
</h3>

```typescript
public monitoringRoleArn: pulumi.Output<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L130">property performanceInsightsEnabled</a>
</h3>

```typescript
public performanceInsightsEnabled: pulumi.Output<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L134">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
public performanceInsightsKmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L138">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The database port

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L143">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L148">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L152">property promotionTier</a>
</h3>

```typescript
public promotionTier: pulumi.Output<number | undefined>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L158">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L162">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean>;
```


Specifies whether the DB cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L166">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L170">property writer</a>
</h3>

```typescript
public writer: pulumi.Output<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L14">class ClusterParameterGroup</a>
</h2>

Provides an RDS DB cluster parameter group resource. Documentation of the available parameters for various Aurora engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L54">constructor</a>
</h3>

```typescript
new ClusterParameterGroup(name: string, args: ClusterParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L38">property family</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L46">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L50">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L54">property tags</a>
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

<h2 class="pdoc-module-header" id="ClusterSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L10">class ClusterSnapshot</a>
</h2>

Manages a RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the [`aws_db_snapshot` resource](https://www.terraform.io/docs/providers/aws/r/db_snapshot.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L76">constructor</a>
</h3>

```typescript
new ClusterSnapshot(name: string, args: ClusterSnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterSnapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L26">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L30">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L34">property dbClusterIdentifier</a>
</h3>

```typescript
public dbClusterIdentifier: pulumi.Output<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L38">property dbClusterSnapshotArn</a>
</h3>

```typescript
public dbClusterSnapshotArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L42">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
public dbClusterSnapshotIdentifier: pulumi.Output<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L46">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L50">property engineVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L54">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L58">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


License model information for the restored DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L62">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


Port that the DB cluster was listening on at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L63">property snapshotType</a>
</h3>

```typescript
public snapshotType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L64">property sourceDbClusterSnapshotArn</a>
</h3>

```typescript
public sourceDbClusterSnapshotArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L68">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The status of this DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L72">property storageEncrypted</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L76">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID associated with the DB cluster snapshot.

<h2 class="pdoc-module-header" id="EventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L12">class EventSubscription</a>
</h2>

Provides a DB event subscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L58">constructor</a>
</h3>

```typescript
new EventSubscription(name: string, args: EventSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L26">property customerAwsId</a>
</h3>

```typescript
public customerAwsId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L30">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L34">property eventCategories</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L46">property snsTopic</a>
</h3>

```typescript
public snsTopic: pulumi.Output<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L50">property sourceIds</a>
</h3>

```typescript
public sourceIds: pulumi.Output<string[] | undefined>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L54">property sourceType</a>
</h3>

```typescript
public sourceType: pulumi.Output<string | undefined>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L58">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L31">class Instance</a>
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
state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L336">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L40">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L47">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L52">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L58">property allowMajorVersionUpgrade</a>
</h3>

```typescript
public allowMajorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L66">property applyImmediately</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L70">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L76">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L80">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L85">property backupRetentionPeriod</a>
</h3>

```typescript
public backupRetentionPeriod: pulumi.Output<number>;
```


The days to retain backups for. Must be
between `0` and `35`. When creating a Read Replica the value must be greater than `0`. [See Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L91">property backupWindow</a>
</h3>

```typescript
public backupWindow: pulumi.Output<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L96">property caCertIdentifier</a>
</h3>

```typescript
public caCertIdentifier: pulumi.Output<string>;
```


Specifies the identifier of the CA certificate for the
DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L104">property characterSetName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L110">property copyTagsToSnapshot</a>
</h3>

```typescript
public copyTagsToSnapshot: pulumi.Output<boolean | undefined>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L120">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L124">property deletionProtection</a>
</h3>

```typescript
public deletionProtection: pulumi.Output<boolean | undefined>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L128">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string | undefined>;
```


The ID of the Directory Service Active Directory domain to create the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L132">property domainIamRoleName</a>
</h3>

```typescript
public domainIamRoleName: pulumi.Output<string | undefined>;
```


The name of the IAM role to be used when making API calls to the Directory Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L136">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
public enabledCloudwatchLogsExports: pulumi.Output<string[] | undefined>;
```


List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L140">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L149">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L157">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L162">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L167">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L173">property iamDatabaseAuthenticationEnabled</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L178">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L183">property identifierPrefix</a>
</h3>

```typescript
public identifierPrefix: pulumi.Output<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L187">property instanceClass</a>
</h3>

```typescript
public instanceClass: pulumi.Output<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L192">property iops</a>
</h3>

```typescript
public iops: pulumi.Output<number | undefined>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L197">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L202">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L210">property maintenanceWindow</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L217">property monitoringInterval</a>
</h3>

```typescript
public monitoringInterval: pulumi.Output<number | undefined>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L225">property monitoringRoleArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L229">property multiAz</a>
</h3>

```typescript
public multiAz: pulumi.Output<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L233">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L237">property optionGroupName</a>
</h3>

```typescript
public optionGroupName: pulumi.Output<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L242">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L248">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L252">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L257">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L258">property replicas</a>
</h3>

```typescript
public replicas: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L268">property replicateSourceDb</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L272">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The RDS Resource ID of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L276">property s3Import</a>
</h3>

```typescript
public s3Import: pulumi.Output<{ ... } | undefined>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L282">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[] | undefined>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L290">property skipFinalSnapshot</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L296">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L300">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The RDS instance status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L307">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L314">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L318">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L326">property timezone</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L331">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L336">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="OptionGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L16">class OptionGroup</a>
</h2>

Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:
* [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
* [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
* [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
* [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L60">constructor</a>
</h3>

```typescript
new OptionGroup(name: string, args: OptionGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OptionGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L25">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db option group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L36">property engineName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L40">property majorEngineVersion</a>
</h3>

```typescript
public majorEngineVersion: pulumi.Output<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L48">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L56">property optionGroupDescription</a>
</h3>

```typescript
public optionGroupDescription: pulumi.Output<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L52">property options</a>
</h3>

```typescript
public options: pulumi.Output<{ ... }[] | undefined>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L60">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L17">class ParameterGroup</a>
</h2>

Provides an RDS DB parameter group resource .Documentation of the available parameters for various RDS engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)
* [MariaDB Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Parameters.html)
* [Oracle Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Oracle.html#USER_ModifyInstance.Oracle.sqlnet)
* [PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Parameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L57">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L26">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L33">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L41">property family</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L49">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L53">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L57">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L15">class SecurityGroup</a>
</h2>

Provides an RDS security group resource. This is only for DB instances in the
EC2-Classic Platform. For instances inside a VPC, use the
[`aws_db_instance.vpc_security_group_ids`](https://www.terraform.io/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
attribute instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L47">constructor</a>
</h3>

```typescript
new SecurityGroup(name: string, args: SecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L24">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The arn of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L35">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L39">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L47">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L10">class Snapshot</a>
</h2>

Manages a RDS database instance snapshot. For managing RDS database cluster snapshots, see the [`aws_db_cluster_snapshot` resource](https://www.terraform.io/docs/providers/aws/r/db_cluster_snapshot.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L92">constructor</a>
</h3>

```typescript
new Snapshot(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Snapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L26">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L30">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L34">property dbInstanceIdentifier</a>
</h3>

```typescript
public dbInstanceIdentifier: pulumi.Output<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L38">property dbSnapshotArn</a>
</h3>

```typescript
public dbSnapshotArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L42">property dbSnapshotIdentifier</a>
</h3>

```typescript
public dbSnapshotIdentifier: pulumi.Output<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L46">property encrypted</a>
</h3>

```typescript
public encrypted: pulumi.Output<boolean>;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L50">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L54">property engineVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L58">property iops</a>
</h3>

```typescript
public iops: pulumi.Output<number>;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L62">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L66">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L70">property optionGroupName</a>
</h3>

```typescript
public optionGroupName: pulumi.Output<string>;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L71">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L72">property snapshotType</a>
</h3>

```typescript
public snapshotType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L76">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
public sourceDbSnapshotIdentifier: pulumi.Output<string>;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L80">property sourceRegion</a>
</h3>

```typescript
public sourceRegion: pulumi.Output<string>;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L84">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L88">property storageType</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L92">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


Specifies the storage type associated with DB snapshot.

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L12">class SubnetGroup</a>
</h2>

Provides an RDS DB subnet group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L48">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L32">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L40">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L44">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L48">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L10">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Provides information about a RDS cluster.

<h2 class="pdoc-module-header" id="getClusterSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L13">function getClusterSnapshot</a>
</h2>

```typescript
getClusterSnapshot(args?: GetClusterSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterSnapshotResult>
```


Use this data source to get information about a DB Cluster Snapshot for use when provisioning DB clusters.

~> **NOTE:** This data source does not apply to snapshots created on DB Instances.
See the [`aws_db_snapshot` data source](https://www.terraform.io/docs/providers/aws/d/db_snapshot.html) for DB Instance snapshots.

<h2 class="pdoc-module-header" id="getEventCategories">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L7">function getEventCategories</a>
</h2>

```typescript
getEventCategories(args?: GetEventCategoriesArgs, opts?: pulumi.InvokeOptions): Promise<GetEventCategoriesResult>
```

<h2 class="pdoc-module-header" id="getInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L10">function getInstance</a>
</h2>

```typescript
getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult>
```


Use this data source to get information about an RDS instance

<h2 class="pdoc-module-header" id="getSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L13">function getSnapshot</a>
</h2>

```typescript
getSnapshot(args?: GetSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetSnapshotResult>
```


Use this data source to get information about a DB Snapshot for use when provisioning DB instances

~> **NOTE:** This data source does not apply to snapshots created on Aurora DB clusters.
See the [`aws_db_cluster_snapshot` data source](https://www.terraform.io/docs/providers/aws/d/db_cluster_snapshot.html) for DB Cluster snapshots.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L466">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L472">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L477">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L481">property backtrackWindow</a>
</h3>

```typescript
backtrackWindow?: pulumi.Input<number>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L485">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L489">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L493">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L497">property clusterMembers</a>
</h3>

```typescript
clusterMembers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L501">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L505">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L509">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L513">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L518">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L522">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L526">property engineMode</a>
</h3>

```typescript
engineMode?: pulumi.Input<string>;
```


The database engine mode. Valid values: `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L530">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version. Updating this argument results in an outage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L536">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L540">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation][6] for availability and limitations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L544">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the RDS Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L548">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L553">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L557">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L561">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L566">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L570">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L574">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L575">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L579">property scalingConfiguration</a>
</h3>

```typescript
scalingConfiguration?: pulumi.Input<{ ... }>;
```


Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L583">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L587">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L591">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L595">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L599">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L604">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L393">interface ClusterInstanceArgs</a>
</h2>

The set of arguments for constructing a ClusterInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L398">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L402">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L406">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L410">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: pulumi.Input<string>;
```


The identifier of the [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L414">property dbParameterGroupName</a>
</h3>

```typescript
dbParameterGroupName?: pulumi.Input<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L418">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L425">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L429">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L433">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L437">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L456">property instanceClass</a>
</h3>

```typescript
instanceClass: pulumi.Input<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes. Please see [AWS Documentation][7] for complete details.
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L460">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L466">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L470">property performanceInsightsEnabled</a>
</h3>

```typescript
performanceInsightsEnabled?: pulumi.Input<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L474">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
performanceInsightsKmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L479">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L484">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L488">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L494">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L498">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the instance.

<h2 class="pdoc-module-header" id="ClusterInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L254">interface ClusterInstanceState</a>
</h2>

Input properties used for looking up and filtering ClusterInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L259">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L263">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of cluster instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L267">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L271">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L275">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The identifier of the [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L279">property dbParameterGroupName</a>
</h3>

```typescript
dbParameterGroupName?: pulumi.Input<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L283">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L287">property dbiResourceId</a>
</h3>

```typescript
dbiResourceId?: pulumi.Input<string>;
```


The region-unique, immutable identifier for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L291">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS address for this instance. May not be writable

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L298">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L302">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L306">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L310">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L329">property instanceClass</a>
</h3>

```typescript
instanceClass?: pulumi.Input<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes. Please see [AWS Documentation][7] for complete details.
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L333">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key if one is set to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L337">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L343">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L347">property performanceInsightsEnabled</a>
</h3>

```typescript
performanceInsightsEnabled?: pulumi.Input<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L351">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
performanceInsightsKmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L355">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The database port

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L360">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L365">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L369">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L375">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L379">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L383">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L387">property writer</a>
</h3>

```typescript
writer?: pulumi.Input<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L129">interface ClusterParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ClusterParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L137">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the DB cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L145">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L149">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L153">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L95">interface ClusterParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ClusterParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L99">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L103">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L107">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the DB cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L115">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L119">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L196">interface ClusterSnapshotArgs</a>
</h2>

The set of arguments for constructing a ClusterSnapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L200">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier: pulumi.Input<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L204">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
dbClusterSnapshotIdentifier: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h2 class="pdoc-module-header" id="ClusterSnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L136">interface ClusterSnapshotState</a>
</h2>

Input properties used for looking up and filtering ClusterSnapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L140">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L144">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L148">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier?: pulumi.Input<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L152">property dbClusterSnapshotArn</a>
</h3>

```typescript
dbClusterSnapshotArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L156">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
dbClusterSnapshotIdentifier?: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L160">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L164">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Version of the database engine for this DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L168">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L172">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


License model information for the restored DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L176">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


Port that the DB cluster was listening on at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L177">property snapshotType</a>
</h3>

```typescript
snapshotType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L178">property sourceDbClusterSnapshotArn</a>
</h3>

```typescript
sourceDbClusterSnapshotArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L182">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status of this DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L186">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterSnapshot.ts#L190">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID associated with the DB cluster snapshot.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L301">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L307">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L311">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L316">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L320">property backtrackWindow</a>
</h3>

```typescript
backtrackWindow?: pulumi.Input<number>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L324">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L328">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L332">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L336">property clusterMembers</a>
</h3>

```typescript
clusterMembers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L340">property clusterResourceId</a>
</h3>

```typescript
clusterResourceId?: pulumi.Input<string>;
```


The RDS Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L344">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L348">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L352">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L356">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L361">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L365">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS address of the RDS instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L369">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L373">property engineMode</a>
</h3>

```typescript
engineMode?: pulumi.Input<string>;
```


The database engine mode. Valid values: `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L377">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version. Updating this argument results in an outage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L383">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L387">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L391">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation][6] for availability and limitations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L395">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the RDS Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L399">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L404">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L408">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L412">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L417">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L421">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L426">property readerEndpoint</a>
</h3>

```typescript
readerEndpoint?: pulumi.Input<string>;
```


A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L430">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L431">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L435">property scalingConfiguration</a>
</h3>

```typescript
scalingConfiguration?: pulumi.Input<{ ... }>;
```


Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L439">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L443">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L447">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L451">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L455">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L460">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="EventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L145">interface EventSubscriptionArgs</a>
</h2>

The set of arguments for constructing a EventSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L149">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L153">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L161">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L165">property snsTopic</a>
</h3>

```typescript
snsTopic: pulumi.Input<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L169">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L173">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L177">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L105">interface EventSubscriptionState</a>
</h2>

Input properties used for looking up and filtering EventSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L106">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L107">property customerAwsId</a>
</h3>

```typescript
customerAwsId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L111">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L115">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L123">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L127">property snsTopic</a>
</h3>

```typescript
snsTopic?: pulumi.Input<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L131">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L135">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L20">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L24">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: string;
```


The cluster identifier of the RDS cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L25">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L31">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L32">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L33">property availabilityZones</a>
</h3>

```typescript
availabilityZones: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L34">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L35">property clusterMembers</a>
</h3>

```typescript
clusterMembers: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L36">property clusterResourceId</a>
</h3>

```typescript
clusterResourceId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L37">property databaseName</a>
</h3>

```typescript
databaseName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L38">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L39">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L40">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L41">property endpoint</a>
</h3>

```typescript
endpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L42">property engine</a>
</h3>

```typescript
engine: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L43">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L44">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L45">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L46">property iamRoles</a>
</h3>

```typescript
iamRoles: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L60">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L47">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L48">property masterUsername</a>
</h3>

```typescript
masterUsername: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L49">property port</a>
</h3>

```typescript
port: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L50">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L51">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L52">property readerEndpoint</a>
</h3>

```typescript
readerEndpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L53">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L54">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L55">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L56">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds: string[];
```

<h2 class="pdoc-module-header" id="GetClusterSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L28">interface GetClusterSnapshotArgs</a>
</h2>

A collection of arguments for invoking getClusterSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L32">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier?: string;
```


Returns the list of snapshots created by the specific db_cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L36">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
dbClusterSnapshotIdentifier?: string;
```


Returns information on a specific snapshot_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L41">property includePublic</a>
</h3>

```typescript
includePublic?: boolean;
```


Set this value to true to include manual DB Cluster Snapshots that are public and can be
copied or restored by any AWS account, otherwise set this value to false. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L47">property includeShared</a>
</h3>

```typescript
includeShared?: boolean;
```


Set this value to true to include shared manual DB Cluster Snapshots from other
AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false.
The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L51">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most recent Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L57">property snapshotType</a>
</h3>

```typescript
snapshotType?: string;
```


The type of snapshots to be returned. If you don't specify a SnapshotType
value, then both automated and manual DB cluster snapshots are returned. Shared and public DB Cluster Snapshots are not
included in the returned results by default. Possible values are, `automated`, `manual`, `shared` and `public`.

<h2 class="pdoc-module-header" id="GetClusterSnapshotResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L63">interface GetClusterSnapshotResult</a>
</h2>

A collection of values returned by getClusterSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L67">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage: number;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L71">property availabilityZones</a>
</h3>

```typescript
availabilityZones: string[];
```


List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L75">property dbClusterSnapshotArn</a>
</h3>

```typescript
dbClusterSnapshotArn: string;
```


The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L79">property engine</a>
</h3>

```typescript
engine: string;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L83">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Version of the database engine for this DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L116">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L87">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L91">property licenseModel</a>
</h3>

```typescript
licenseModel: string;
```


License model information for the restored DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L95">property port</a>
</h3>

```typescript
port: number;
```


Port that the DB cluster was listening on at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L99">property snapshotCreateTime</a>
</h3>

```typescript
snapshotCreateTime: string;
```


Time when the snapshot was taken, in Universal Coordinated Time (UTC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L100">property sourceDbClusterSnapshotArn</a>
</h3>

```typescript
sourceDbClusterSnapshotArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L104">property status</a>
</h3>

```typescript
status: string;
```


The status of this DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L108">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted: boolean;
```


Specifies whether the DB cluster snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getClusterSnapshot.ts#L112">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


The VPC ID associated with the DB cluster snapshot.

<h2 class="pdoc-module-header" id="GetEventCategoriesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L17">interface GetEventCategoriesArgs</a>
</h2>

A collection of arguments for invoking getEventCategories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L21">property sourceType</a>
</h3>

```typescript
sourceType?: string;
```


The type of source that will be generating the events. Valid options are db-instance, db-security-group, db-parameter-group, db-snapshot, db-cluster or db-cluster-snapshot.

<h2 class="pdoc-module-header" id="GetEventCategoriesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L27">interface GetEventCategoriesResult</a>
</h2>

A collection of values returned by getEventCategories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L31">property eventCategories</a>
</h3>

```typescript
eventCategories: string[];
```


A list of the event categories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getEventCategories.ts#L35">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L19">interface GetInstanceArgs</a>
</h2>

A collection of arguments for invoking getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L23">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier: string;
```


The name of the RDS instance

<h2 class="pdoc-module-header" id="GetInstanceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L29">interface GetInstanceResult</a>
</h2>

A collection of values returned by getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L33">property address</a>
</h3>

```typescript
address: string;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L37">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage: number;
```


Specifies the allocated storage size specified in gigabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L41">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade: boolean;
```


Indicates that minor version patches are applied automatically.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L45">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


Specifies the name of the Availability Zone the DB instance is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L49">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod: number;
```


Specifies the number of days for which automatic DB snapshots are retained.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L53">property caCertIdentifier</a>
</h3>

```typescript
caCertIdentifier: string;
```


Specifies the identifier of the CA certificate for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L57">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier: string;
```


If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L61">property dbInstanceArn</a>
</h3>

```typescript
dbInstanceArn: string;
```


The Amazon Resource Name (ARN) for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L65">property dbInstanceClass</a>
</h3>

```typescript
dbInstanceClass: string;
```


Contains the name of the compute and memory capacity class of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L69">property dbInstancePort</a>
</h3>

```typescript
dbInstancePort: number;
```


Specifies the port that the DB instance listens on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L73">property dbName</a>
</h3>

```typescript
dbName: string;
```


Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L77">property dbParameterGroups</a>
</h3>

```typescript
dbParameterGroups: string[];
```


Provides the list of DB parameter groups applied to this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L81">property dbSecurityGroups</a>
</h3>

```typescript
dbSecurityGroups: string[];
```


Provides List of DB security groups associated to this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L85">property dbSubnetGroup</a>
</h3>

```typescript
dbSubnetGroup: string;
```


Specifies the name of the subnet group associated with the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L89">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports: string[];
```


List of log types to export to cloudwatch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L93">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L97">property engine</a>
</h3>

```typescript
engine: string;
```


Provides the name of the database engine to be used for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L101">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Indicates the database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L105">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId: string;
```


The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L177">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L109">property iops</a>
</h3>

```typescript
iops: number;
```


Specifies the Provisioned IOPS (I/O operations per second) value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L113">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L117">property licenseModel</a>
</h3>

```typescript
licenseModel: string;
```


License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L121">property masterUsername</a>
</h3>

```typescript
masterUsername: string;
```


Contains the master username for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L125">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval: number;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L129">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn: string;
```


The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L133">property multiAz</a>
</h3>

```typescript
multiAz: boolean;
```


Specifies if the DB instance is a Multi-AZ deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L137">property optionGroupMemberships</a>
</h3>

```typescript
optionGroupMemberships: string[];
```


Provides the list of option group memberships for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L141">property port</a>
</h3>

```typescript
port: number;
```


The database port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L145">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow: string;
```


Specifies the daily time range during which automated backups are created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L149">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow: string;
```


Specifies the weekly time range during which system maintenance can occur in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L153">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible: boolean;
```


Specifies the accessibility options for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L157">property replicateSourceDb</a>
</h3>

```typescript
replicateSourceDb: string;
```


The identifier of the source DB that this is a replica of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L161">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted: boolean;
```


Specifies whether the DB instance is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L165">property storageType</a>
</h3>

```typescript
storageType: string;
```


Specifies the storage type associated with DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L169">property timezone</a>
</h3>

```typescript
timezone: string;
```


The time zone of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L173">property vpcSecurityGroups</a>
</h3>

```typescript
vpcSecurityGroups: string[];
```


Provides a list of VPC security group elements that the DB instance belongs to.

<h2 class="pdoc-module-header" id="GetSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L28">interface GetSnapshotArgs</a>
</h2>

A collection of arguments for invoking getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L32">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier?: string;
```


Returns the list of snapshots created by the specific db_instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L36">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier?: string;
```


Returns information on a specific snapshot_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L41">property includePublic</a>
</h3>

```typescript
includePublic?: boolean;
```


Set this value to true to include manual DB snapshots that are public and can be
copied or restored by any AWS account, otherwise set this value to false. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L47">property includeShared</a>
</h3>

```typescript
includeShared?: boolean;
```


Set this value to true to include shared manual DB snapshots from other
AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false.
The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L52">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most
recent Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L58">property snapshotType</a>
</h3>

```typescript
snapshotType?: string;
```


The type of snapshots to be returned. If you don't specify a SnapshotType
value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not
included in the returned results by default. Possible values are, `automated`, `manual`, `shared` and `public`.

<h2 class="pdoc-module-header" id="GetSnapshotResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L64">interface GetSnapshotResult</a>
</h2>

A collection of values returned by getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L68">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage: number;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L72">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L76">property dbSnapshotArn</a>
</h3>

```typescript
dbSnapshotArn: string;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L80">property encrypted</a>
</h3>

```typescript
encrypted: boolean;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L84">property engine</a>
</h3>

```typescript
engine: string;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L88">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Specifies the version of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L133">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L92">property iops</a>
</h3>

```typescript
iops: number;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L96">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L100">property licenseModel</a>
</h3>

```typescript
licenseModel: string;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L104">property optionGroupName</a>
</h3>

```typescript
optionGroupName: string;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L105">property port</a>
</h3>

```typescript
port: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L109">property snapshotCreateTime</a>
</h3>

```typescript
snapshotCreateTime: string;
```


Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L113">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
sourceDbSnapshotIdentifier: string;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L117">property sourceRegion</a>
</h3>

```typescript
sourceRegion: string;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L121">property status</a>
</h3>

```typescript
status: string;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L125">property storageType</a>
</h3>

```typescript
storageType: string;
```


Specifies the storage type associated with DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L129">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


Specifies the ID of the VPC associated with the DB snapshot.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L768">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L773">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L779">property allowMajorVersionUpgrade</a>
</h3>

```typescript
allowMajorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L787">property applyImmediately</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L793">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L797">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L802">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Must be
between `0` and `35`. When creating a Read Replica the value must be greater than `0`. [See Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L808">property backupWindow</a>
</h3>

```typescript
backupWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L816">property characterSetName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L822">property copyTagsToSnapshot</a>
</h3>

```typescript
copyTagsToSnapshot?: pulumi.Input<boolean>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L832">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L836">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L840">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The ID of the Directory Service Active Directory domain to create the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L844">property domainIamRoleName</a>
</h3>

```typescript
domainIamRoleName?: pulumi.Input<string>;
```


The name of the IAM role to be used when making API calls to the Directory Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L848">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L857">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L865">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L870">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L876">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L881">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L886">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L890">property instanceClass</a>
</h3>

```typescript
instanceClass: pulumi.Input<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L895">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L900">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L905">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L913">property maintenanceWindow</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L920">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L928">property monitoringRoleArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L932">property multiAz</a>
</h3>

```typescript
multiAz?: pulumi.Input<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L936">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L940">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L945">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L951">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L955">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L960">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L970">property replicateSourceDb</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L974">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L980">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L988">property skipFinalSnapshot</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L994">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1001">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1008">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1012">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1020">property timezone</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1025">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L1030">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L469">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L473">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L478">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L484">property allowMajorVersionUpgrade</a>
</h3>

```typescript
allowMajorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L492">property applyImmediately</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L496">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L502">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L506">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L511">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Must be
between `0` and `35`. When creating a Read Replica the value must be greater than `0`. [See Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L517">property backupWindow</a>
</h3>

```typescript
backupWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L522">property caCertIdentifier</a>
</h3>

```typescript
caCertIdentifier?: pulumi.Input<string>;
```


Specifies the identifier of the CA certificate for the
DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L530">property characterSetName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L536">property copyTagsToSnapshot</a>
</h3>

```typescript
copyTagsToSnapshot?: pulumi.Input<boolean>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L546">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L550">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L554">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The ID of the Directory Service Active Directory domain to create the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L558">property domainIamRoleName</a>
</h3>

```typescript
domainIamRoleName?: pulumi.Input<string>;
```


The name of the IAM role to be used when making API calls to the Directory Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L562">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L566">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L575">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L583">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L588">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L593">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L599">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L604">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L609">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L613">property instanceClass</a>
</h3>

```typescript
instanceClass?: pulumi.Input<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L618">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L623">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L628">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L636">property maintenanceWindow</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L643">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L651">property monitoringRoleArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L655">property multiAz</a>
</h3>

```typescript
multiAz?: pulumi.Input<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L659">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L663">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L668">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L674">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L678">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L683">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L684">property replicas</a>
</h3>

```typescript
replicas?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L694">property replicateSourceDb</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L698">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The RDS Resource ID of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L702">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L708">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L716">property skipFinalSnapshot</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L722">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L726">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The RDS instance status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L733">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L740">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L744">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L752">property timezone</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L757">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L762">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="OptionGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L144">interface OptionGroupArgs</a>
</h2>

The set of arguments for constructing a OptionGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L148">property engineName</a>
</h3>

```typescript
engineName: pulumi.Input<string>;
```


Specifies the name of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L152">property majorEngineVersion</a>
</h3>

```typescript
majorEngineVersion: pulumi.Input<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L160">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L168">property optionGroupDescription</a>
</h3>

```typescript
optionGroupDescription?: pulumi.Input<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L164">property options</a>
</h3>

```typescript
options?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L172">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="OptionGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L106">interface OptionGroupState</a>
</h2>

Input properties used for looking up and filtering OptionGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L110">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db option group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L114">property engineName</a>
</h3>

```typescript
engineName?: pulumi.Input<string>;
```


Specifies the name of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L118">property majorEngineVersion</a>
</h3>

```typescript
majorEngineVersion?: pulumi.Input<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L126">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L134">property optionGroupDescription</a>
</h3>

```typescript
optionGroupDescription?: pulumi.Input<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L130">property options</a>
</h3>

```typescript
options?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L138">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L132">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L140">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the DB parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L148">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L152">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L156">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L98">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L102">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L110">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the DB parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L118">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L122">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L126">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L110">interface SecurityGroupArgs</a>
</h2>

The set of arguments for constructing a SecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L114">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L118">property ingress</a>
</h3>

```typescript
ingress: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L126">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L84">interface SecurityGroupState</a>
</h2>

Input properties used for looking up and filtering SecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L88">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The arn of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L96">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L104">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L236">interface SnapshotArgs</a>
</h2>

The set of arguments for constructing a Snapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L240">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier: pulumi.Input<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L244">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h2 class="pdoc-module-header" id="SnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L160">interface SnapshotState</a>
</h2>

Input properties used for looking up and filtering Snapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L164">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L168">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L172">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier?: pulumi.Input<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L176">property dbSnapshotArn</a>
</h3>

```typescript
dbSnapshotArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L180">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier?: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L184">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L188">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L192">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Specifies the version of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L196">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L200">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L204">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L208">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L209">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L210">property snapshotType</a>
</h3>

```typescript
snapshotType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L214">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
sourceDbSnapshotIdentifier?: pulumi.Input<string>;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L218">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L222">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L226">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


Specifies the storage type associated with DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L230">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


Specifies the storage type associated with DB snapshot.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L117">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L129">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L133">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L137">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L87">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L103">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L107">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

