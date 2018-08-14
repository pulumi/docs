---
title: Module redshift
---

<a href="../index.html">@pulumi/aws</a> &gt; redshift

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#SecurityGroup">class SecurityGroup</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getServiceAccount">function getServiceAccount</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetServiceAccountArgs">interface GetServiceAccountArgs</a>
* <a href="#GetServiceAccountResult">interface GetServiceAccountResult</a>
* <a href="#ParameterGroupArgs">interface ParameterGroupArgs</a>
* <a href="#ParameterGroupState">interface ParameterGroupState</a>
* <a href="#SecurityGroupArgs">interface SecurityGroupArgs</a>
* <a href="#SecurityGroupState">interface SecurityGroupState</a>
* <a href="#SubnetGroupArgs">interface SubnetGroupArgs</a>
* <a href="#SubnetGroupState">interface SubnetGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts">redshift/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts">redshift/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts">redshift/getServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts">redshift/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts">redshift/securityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts">redshift/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L14">class Cluster</a>
</h2>

Provides a Redshift Cluster Resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L183">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L30">property allowVersionUpgrade</a>
</h3>

```typescript
public allowVersionUpgrade: pulumi.Output<boolean | undefined>;
```


If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L34">property automatedSnapshotRetentionPeriod</a>
</h3>

```typescript
public automatedSnapshotRetentionPeriod: pulumi.Output<number | undefined>;
```


The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L38">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L43">property bucketName</a>
</h3>

```typescript
public bucketName: pulumi.Output<string>;
```


The name of an existing S3 bucket where the log files are to be stored. Must be in the same region as the cluster and the cluster must have read bucket and put object permissions.
For more information on the permissions required for the bucket, please read the AWS [documentation](http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L48">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The Cluster Identifier. Must be a lower case
string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L52">property clusterParameterGroupName</a>
</h3>

```typescript
public clusterParameterGroupName: pulumi.Output<string>;
```


The name of the parameter group to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L56">property clusterPublicKey</a>
</h3>

```typescript
public clusterPublicKey: pulumi.Output<string>;
```


The public key for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L60">property clusterRevisionNumber</a>
</h3>

```typescript
public clusterRevisionNumber: pulumi.Output<string>;
```


The specific revision number of the database in the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L64">property clusterSecurityGroups</a>
</h3>

```typescript
public clusterSecurityGroups: pulumi.Output<string[]>;
```


A list of security groups to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L68">property clusterSubnetGroupName</a>
</h3>

```typescript
public clusterSubnetGroupName: pulumi.Output<string>;
```


The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L72">property clusterType</a>
</h3>

```typescript
public clusterType: pulumi.Output<string>;
```


The cluster type to use. Either `single-node` or `multi-node`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L77">property clusterVersion</a>
</h3>

```typescript
public clusterVersion: pulumi.Output<string | undefined>;
```


The version of the Amazon Redshift engine software that you want to deploy on the cluster.
The version selected runs on all the nodes in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L82">property databaseName</a>
</h3>

```typescript
public databaseName: pulumi.Output<string>;
```


The name of the first database to be created when the cluster is created.
If you do not provide a name, Amazon Redshift will create a default database called `dev`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L86">property dnsName</a>
</h3>

```typescript
public dnsName: pulumi.Output<string>;
```


The DNS name of the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L90">property elasticIp</a>
</h3>

```typescript
public elasticIp: pulumi.Output<string | undefined>;
```


The Elastic IP (EIP) address for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L91">property enableLogging</a>
</h3>

```typescript
public enableLogging: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L95">property encrypted</a>
</h3>

```typescript
public encrypted: pulumi.Output<boolean>;
```


If true , the data in the cluster is encrypted at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L99">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The connection endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L103">property enhancedVpcRouting</a>
</h3>

```typescript
public enhancedVpcRouting: pulumi.Output<boolean>;
```


If true , enhanced VPC routing is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L107">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `skip_final_snapshot` must be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L111">property iamRoles</a>
</h3>

```typescript
public iamRoles: pulumi.Output<string[]>;
```


A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L115">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L119">property logging</a>
</h3>

```typescript
public logging: pulumi.Output<{ ... } | undefined>;
```


Logging, documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L125">property masterPassword</a>
</h3>

```typescript
public masterPassword: pulumi.Output<string | undefined>;
```


Password for the master DB user.
Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
contain at least one uppercase letter, one lowercase letter, and one number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L129">property masterUsername</a>
</h3>

```typescript
public masterUsername: pulumi.Output<string | undefined>;
```


Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L133">property nodeType</a>
</h3>

```typescript
public nodeType: pulumi.Output<string>;
```


The node type to be provisioned for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L137">property numberOfNodes</a>
</h3>

```typescript
public numberOfNodes: pulumi.Output<number | undefined>;
```


The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L141">property ownerAccount</a>
</h3>

```typescript
public ownerAccount: pulumi.Output<string | undefined>;
```


The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L146">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port number on which the cluster accepts incoming connections.
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L151">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The weekly time range (in UTC) during which automated cluster maintenance can occur.
Format: ddd:hh24:mi-ddd:hh24:mi

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L155">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


If true, the cluster can be accessed from a public network. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L159">property s3KeyPrefix</a>
</h3>

```typescript
public s3KeyPrefix: pulumi.Output<string>;
```


The prefix applied to the log file names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L163">property skipFinalSnapshot</a>
</h3>

```typescript
public skipFinalSnapshot: pulumi.Output<boolean | undefined>;
```


Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L167">property snapshotClusterIdentifier</a>
</h3>

```typescript
public snapshotClusterIdentifier: pulumi.Output<string | undefined>;
```


The name of the cluster the source snapshot was created from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L171">property snapshotCopy</a>
</h3>

```typescript
public snapshotCopy: pulumi.Output<{ ... } | undefined>;
```


Configuration of automatic copy of snapshots from one region to another. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L175">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of the snapshot from which to create the new cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L179">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L183">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

<h2 class="pdoc-module-header" id="ParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L9">class ParameterGroup</a>
</h2>

Provides a Redshift Cluster parameter group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L37">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the Redshift parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L29">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the Redshift parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Redshift parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L37">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of Redshift parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L9">class SecurityGroup</a>
</h2>

Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L33">constructor</a>
</h3>

```typescript
new SecurityGroup(name: string, args: SecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the Redshift security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L29">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Redshift security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L11">class SubnetGroup</a>
</h2>

Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L39">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L27">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the Redshift Subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Redshift Subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L35">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


An array of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L39">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L9">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Provides details about a specific redshift cluster.

<h2 class="pdoc-module-header" id="getServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L10">function getServiceAccount</a>
</h2>

```typescript
getServiceAccount(args?: GetServiceAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceAccountResult>
```


Use this data source to get the Account ID of the [AWS Redshift Service Account](http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging)
in a given region for the purpose of allowing Redshift to store audit data in S3.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L452">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L456">property allowVersionUpgrade</a>
</h3>

```typescript
allowVersionUpgrade?: pulumi.Input<boolean>;
```


If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L460">property automatedSnapshotRetentionPeriod</a>
</h3>

```typescript
automatedSnapshotRetentionPeriod?: pulumi.Input<number>;
```


The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L464">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L469">property bucketName</a>
</h3>

```typescript
bucketName?: pulumi.Input<string>;
```


The name of an existing S3 bucket where the log files are to be stored. Must be in the same region as the cluster and the cluster must have read bucket and put object permissions.
For more information on the permissions required for the bucket, please read the AWS [documentation](http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L474">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: pulumi.Input<string>;
```


The Cluster Identifier. Must be a lower case
string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L478">property clusterParameterGroupName</a>
</h3>

```typescript
clusterParameterGroupName?: pulumi.Input<string>;
```


The name of the parameter group to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L482">property clusterPublicKey</a>
</h3>

```typescript
clusterPublicKey?: pulumi.Input<string>;
```


The public key for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L486">property clusterRevisionNumber</a>
</h3>

```typescript
clusterRevisionNumber?: pulumi.Input<string>;
```


The specific revision number of the database in the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L490">property clusterSecurityGroups</a>
</h3>

```typescript
clusterSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security groups to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L494">property clusterSubnetGroupName</a>
</h3>

```typescript
clusterSubnetGroupName?: pulumi.Input<string>;
```


The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L498">property clusterType</a>
</h3>

```typescript
clusterType?: pulumi.Input<string>;
```


The cluster type to use. Either `single-node` or `multi-node`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L503">property clusterVersion</a>
</h3>

```typescript
clusterVersion?: pulumi.Input<string>;
```


The version of the Amazon Redshift engine software that you want to deploy on the cluster.
The version selected runs on all the nodes in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L508">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


The name of the first database to be created when the cluster is created.
If you do not provide a name, Amazon Redshift will create a default database called `dev`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L512">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```


The Elastic IP (EIP) address for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L513">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L517">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


If true , the data in the cluster is encrypted at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L521">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The connection endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L525">property enhancedVpcRouting</a>
</h3>

```typescript
enhancedVpcRouting?: pulumi.Input<boolean>;
```


If true , enhanced VPC routing is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L529">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `skip_final_snapshot` must be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L533">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L537">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L541">property logging</a>
</h3>

```typescript
logging?: pulumi.Input<{ ... }>;
```


Logging, documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L547">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user.
Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
contain at least one uppercase letter, one lowercase letter, and one number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L551">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L555">property nodeType</a>
</h3>

```typescript
nodeType: pulumi.Input<string>;
```


The node type to be provisioned for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L559">property numberOfNodes</a>
</h3>

```typescript
numberOfNodes?: pulumi.Input<number>;
```


The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L563">property ownerAccount</a>
</h3>

```typescript
ownerAccount?: pulumi.Input<string>;
```


The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L568">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which the cluster accepts incoming connections.
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L573">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range (in UTC) during which automated cluster maintenance can occur.
Format: ddd:hh24:mi-ddd:hh24:mi

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L577">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


If true, the cluster can be accessed from a public network. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L581">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix applied to the log file names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L585">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L589">property snapshotClusterIdentifier</a>
</h3>

```typescript
snapshotClusterIdentifier?: pulumi.Input<string>;
```


The name of the cluster the source snapshot was created from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L593">property snapshotCopy</a>
</h3>

```typescript
snapshotCopy?: pulumi.Input<{ ... }>;
```


Configuration of automatic copy of snapshots from one region to another. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L597">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


The name of the snapshot from which to create the new cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L601">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L605">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L289">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L293">property allowVersionUpgrade</a>
</h3>

```typescript
allowVersionUpgrade?: pulumi.Input<boolean>;
```


If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L297">property automatedSnapshotRetentionPeriod</a>
</h3>

```typescript
automatedSnapshotRetentionPeriod?: pulumi.Input<number>;
```


The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L301">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L306">property bucketName</a>
</h3>

```typescript
bucketName?: pulumi.Input<string>;
```


The name of an existing S3 bucket where the log files are to be stored. Must be in the same region as the cluster and the cluster must have read bucket and put object permissions.
For more information on the permissions required for the bucket, please read the AWS [documentation](http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L311">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The Cluster Identifier. Must be a lower case
string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L315">property clusterParameterGroupName</a>
</h3>

```typescript
clusterParameterGroupName?: pulumi.Input<string>;
```


The name of the parameter group to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L319">property clusterPublicKey</a>
</h3>

```typescript
clusterPublicKey?: pulumi.Input<string>;
```


The public key for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L323">property clusterRevisionNumber</a>
</h3>

```typescript
clusterRevisionNumber?: pulumi.Input<string>;
```


The specific revision number of the database in the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L327">property clusterSecurityGroups</a>
</h3>

```typescript
clusterSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security groups to be associated with this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L331">property clusterSubnetGroupName</a>
</h3>

```typescript
clusterSubnetGroupName?: pulumi.Input<string>;
```


The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L335">property clusterType</a>
</h3>

```typescript
clusterType?: pulumi.Input<string>;
```


The cluster type to use. Either `single-node` or `multi-node`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L340">property clusterVersion</a>
</h3>

```typescript
clusterVersion?: pulumi.Input<string>;
```


The version of the Amazon Redshift engine software that you want to deploy on the cluster.
The version selected runs on all the nodes in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L345">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


The name of the first database to be created when the cluster is created.
If you do not provide a name, Amazon Redshift will create a default database called `dev`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L349">property dnsName</a>
</h3>

```typescript
dnsName?: pulumi.Input<string>;
```


The DNS name of the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L353">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```


The Elastic IP (EIP) address for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L354">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L358">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


If true , the data in the cluster is encrypted at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L362">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The connection endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L366">property enhancedVpcRouting</a>
</h3>

```typescript
enhancedVpcRouting?: pulumi.Input<boolean>;
```


If true , enhanced VPC routing is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L370">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `skip_final_snapshot` must be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L374">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L378">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L382">property logging</a>
</h3>

```typescript
logging?: pulumi.Input<{ ... }>;
```


Logging, documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L388">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user.
Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
contain at least one uppercase letter, one lowercase letter, and one number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L392">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L396">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The node type to be provisioned for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L400">property numberOfNodes</a>
</h3>

```typescript
numberOfNodes?: pulumi.Input<number>;
```


The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L404">property ownerAccount</a>
</h3>

```typescript
ownerAccount?: pulumi.Input<string>;
```


The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L409">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which the cluster accepts incoming connections.
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L414">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range (in UTC) during which automated cluster maintenance can occur.
Format: ddd:hh24:mi-ddd:hh24:mi

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L418">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


If true, the cluster can be accessed from a public network. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L422">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix applied to the log file names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L426">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L430">property snapshotClusterIdentifier</a>
</h3>

```typescript
snapshotClusterIdentifier?: pulumi.Input<string>;
```


The name of the cluster the source snapshot was created from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L434">property snapshotCopy</a>
</h3>

```typescript
snapshotCopy?: pulumi.Input<{ ... }>;
```


Configuration of automatic copy of snapshots from one region to another. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L438">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


The name of the snapshot from which to create the new cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L442">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/cluster.ts#L446">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L19">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L23">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: string;
```


The cluster identifier

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L24">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L30">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L34">property allowVersionUpgrade</a>
</h3>

```typescript
allowVersionUpgrade: boolean;
```


Whether major version upgrades can be applied during maintenance period

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L38">property automatedSnapshotRetentionPeriod</a>
</h3>

```typescript
automatedSnapshotRetentionPeriod: number;
```


The backup retention period

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L42">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


The availability zone of the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L46">property bucketName</a>
</h3>

```typescript
bucketName: string;
```


The name of the S3 bucket where the log files are to be stored

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L50">property clusterParameterGroupName</a>
</h3>

```typescript
clusterParameterGroupName: string;
```


The name of the parameter group to be associated with this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L54">property clusterPublicKey</a>
</h3>

```typescript
clusterPublicKey: string;
```


The public key for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L58">property clusterRevisionNumber</a>
</h3>

```typescript
clusterRevisionNumber: string;
```


The cluster revision number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L62">property clusterSecurityGroups</a>
</h3>

```typescript
clusterSecurityGroups: string[];
```


The security groups associated with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L66">property clusterSubnetGroupName</a>
</h3>

```typescript
clusterSubnetGroupName: string;
```


The name of a cluster subnet group to be associated with this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L70">property clusterType</a>
</h3>

```typescript
clusterType: string;
```


The cluster type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L71">property clusterVersion</a>
</h3>

```typescript
clusterVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L75">property databaseName</a>
</h3>

```typescript
databaseName: string;
```


The name of the default database in the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L79">property elasticIp</a>
</h3>

```typescript
elasticIp: string;
```


The Elastic IP of the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L83">property enableLogging</a>
</h3>

```typescript
enableLogging: boolean;
```


Whether cluster logging is enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L87">property encrypted</a>
</h3>

```typescript
encrypted: boolean;
```


Whether the cluster data is encrypted

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L91">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The cluster endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L95">property enhancedVpcRouting</a>
</h3>

```typescript
enhancedVpcRouting: boolean;
```


Whether enhanced VPC routing is enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L99">property iamRoles</a>
</h3>

```typescript
iamRoles: string[];
```


The IAM roles associated to the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L143">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L103">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


The KMS encryption key associated to the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L107">property masterUsername</a>
</h3>

```typescript
masterUsername: string;
```


Username for the master DB user

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L111">property nodeType</a>
</h3>

```typescript
nodeType: string;
```


The cluster node type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L115">property numberOfNodes</a>
</h3>

```typescript
numberOfNodes: number;
```


The number of nodes in the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L119">property port</a>
</h3>

```typescript
port: number;
```


The port the cluster responds on

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L123">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow: string;
```


The maintenance window

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L127">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible: boolean;
```


Whether the cluster is publicly accessible

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L131">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix: string;
```


The folder inside the S3 bucket where the log files are stored

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L135">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


The VPC Id associated with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getCluster.ts#L139">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds: string[];
```


The VPC security group Ids associated with the cluster

<h2 class="pdoc-module-header" id="GetServiceAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L20">interface GetServiceAccountArgs</a>
</h2>

A collection of arguments for invoking getServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L25">property region</a>
</h3>

```typescript
region?: string;
```


Name of the region whose AWS Redshift account ID is desired.
Defaults to the region from the AWS provider configuration.

<h2 class="pdoc-module-header" id="GetServiceAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L31">interface GetServiceAccountResult</a>
</h2>

A collection of values returned by getServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the AWS Redshift service account in the selected region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/getServiceAccount.ts#L39">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L94">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L102">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the Redshift parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L110">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Redshift parameters to apply.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L72">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L76">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L80">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the Redshift parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/parameterGroup.ts#L88">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Redshift parameters to apply.

<h2 class="pdoc-module-header" id="SecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L84">interface SecurityGroupArgs</a>
</h2>

The set of arguments for constructing a SecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L88">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L92">property ingress</a>
</h3>

```typescript
ingress: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift security group.

<h2 class="pdoc-module-header" id="SecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L66">interface SecurityGroupState</a>
</h2>

Input properties used for looking up and filtering SecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L70">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L74">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/securityGroup.ts#L78">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift security group.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L96">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L100">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift Subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift Subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L108">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


An array of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L112">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L74">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L78">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Redshift Subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Redshift Subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L86">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/redshift/subnetGroup.ts#L90">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

