
---
title: "Cluster"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages a [RDS Aurora Cluster][2]. To manage cluster instances that inherit configuration from the cluster (when not running the cluster in `serverless` engine mode), see the [`aws.rds.ClusterInstance` resource](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html). To manage non-Aurora databases (e.g. MySQL, PostgreSQL, SQL Server, etc.), see the [`aws.rds.Instance` resource](https://www.terraform.io/docs/providers/aws/r/db_instance.html).

For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

Changes to a RDS Cluster can occur when you manually change a
parameter, such as `port`, and are reflected in the next maintenance
window. Because of this, this provider may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

> **Note:** using `apply_immediately` can result in a
brief downtime as the server reboots. See the AWS Docs on [RDS Maintenance][4]
for more information.

> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Example Usage

### Aurora MySQL 2.x (MySQL 5.7)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const defaultCluster = new aws.rds.Cluster("default", {
    availabilityZones: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    backupRetentionPeriod: 5,
    clusterIdentifier: "aurora-cluster-demo",
    databaseName: "mydb",
    engine: "aurora-mysql",
    engineVersion: "5.7.mysql_aurora.2.03.2",
    masterPassword: "bar",
    masterUsername: "foo",
    preferredBackupWindow: "07:00-09:00",
});
```

### Aurora MySQL 1.x (MySQL 5.6)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const defaultCluster = new aws.rds.Cluster("default", {
    availabilityZones: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    backupRetentionPeriod: 5,
    clusterIdentifier: "aurora-cluster-demo",
    databaseName: "mydb",
    masterPassword: "bar",
    masterUsername: "foo",
    preferredBackupWindow: "07:00-09:00",
});
```

### Aurora with PostgreSQL engine

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const postgresql = new aws.rds.Cluster("postgresql", {
    availabilityZones: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    backupRetentionPeriod: 5,
    clusterIdentifier: "aurora-cluster-demo",
    databaseName: "mydb",
    engine: "aurora-postgresql",
    masterPassword: "bar",
    masterUsername: "foo",
    preferredBackupWindow: "07:00-09:00",
});
```

### Aurora Multi-Master Cluster

> More information about Aurora Multi-Master Clusters can be found in the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-multi-master.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.rds.Cluster("example", {
    clusterIdentifier: "example",
    dbSubnetGroupName: aws_db_subnet_group_example.name,
    engineMode: "multimaster",
    masterPassword: "barbarbarbar",
    masterUsername: "foo",
    skipFinalSnapshot: true,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster.html.markdown.



## Create a Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, id, opts=None, </span>apply_immediately=None<span class="p">, </span>availability_zones=None<span class="p">, </span>backtrack_window=None<span class="p">, </span>backup_retention_period=None<span class="p">, </span>cluster_identifier=None<span class="p">, </span>cluster_identifier_prefix=None<span class="p">, </span>cluster_members=None<span class="p">, </span>copy_tags_to_snapshot=None<span class="p">, </span>database_name=None<span class="p">, </span>db_cluster_parameter_group_name=None<span class="p">, </span>db_subnet_group_name=None<span class="p">, </span>deletion_protection=None<span class="p">, </span>enable_http_endpoint=None<span class="p">, </span>enabled_cloudwatch_logs_exports=None<span class="p">, </span>engine=None<span class="p">, </span>engine_mode=None<span class="p">, </span>engine_version=None<span class="p">, </span>final_snapshot_identifier=None<span class="p">, </span>global_cluster_identifier=None<span class="p">, </span>iam_database_authentication_enabled=None<span class="p">, </span>iam_roles=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>master_password=None<span class="p">, </span>master_username=None<span class="p">, </span>port=None<span class="p">, </span>preferred_backup_window=None<span class="p">, </span>preferred_maintenance_window=None<span class="p">, </span>replication_source_identifier=None<span class="p">, </span>s3_import=None<span class="p">, </span>scaling_configuration=None<span class="p">, </span>skip_final_snapshot=None<span class="p">, </span>snapshot_identifier=None<span class="p">, </span>source_region=None<span class="p">, </span>storage_encrypted=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_security_group_ids=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.ClusterArgs.html">ClusterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Cluster resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>S3Import<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">*rds.<wbr>Cluster<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">*rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>Engine<wbr>Type?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>Engine<wbr>Mode?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">rds.<wbr>Cluster<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack_<wbr>window</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>members</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy_<wbr>tags_<wbr>to_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>cluster_<wbr>parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion_<wbr>protection</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>http_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final_<wbr>snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>database_<wbr>authentication_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>roles</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>source_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">dict{cluster_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">dict{cluster_<wbr>scaling_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip_<wbr>final_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Cluster Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">*rds.<wbr>Cluster<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">*rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>Engine<wbr>Type?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>Engine<wbr>Mode?</code>
            </td>
            <td class="align-top">{{% md %}} The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">rds.<wbr>Cluster<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack_<wbr>window</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>members</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy_<wbr>tags_<wbr>to_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>cluster_<wbr>parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion_<wbr>protection</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>http_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final_<wbr>snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>database_<wbr>authentication_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>roles</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reader_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>source_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">dict{cluster_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">dict{cluster_<wbr>scaling_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip_<wbr>final_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Cluster Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster;
```

```python
def get(resource_name, id, opts=None, apply_<wbr>immediately=None, arn=None, availability_<wbr>zones=None, backtrack_<wbr>window=None, backup_<wbr>retention_<wbr>period=None, cluster_<wbr>identifier=None, cluster_<wbr>identifier_<wbr>prefix=None, cluster_<wbr>members=None, cluster_<wbr>resource_<wbr>id=None, copy_<wbr>tags_<wbr>to_<wbr>snapshot=None, database_<wbr>name=None, db_<wbr>cluster_<wbr>parameter_<wbr>group_<wbr>name=None, db_<wbr>subnet_<wbr>group_<wbr>name=None, deletion_<wbr>protection=None, enable_<wbr>http_<wbr>endpoint=None, enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports=None, endpoint=None, engine=None, engine_<wbr>mode=None, engine_<wbr>version=None, final_<wbr>snapshot_<wbr>identifier=None, global_<wbr>cluster_<wbr>identifier=None, hosted_<wbr>zone_<wbr>id=None, iam_<wbr>database_<wbr>authentication_<wbr>enabled=None, iam_<wbr>roles=None, kms_<wbr>key_<wbr>id=None, master_<wbr>password=None, master_<wbr>username=None, port=None, preferred_<wbr>backup_<wbr>window=None, preferred_<wbr>maintenance_<wbr>window=None, reader_<wbr>endpoint=None, replication_<wbr>source_<wbr>identifier=None, s3_<wbr>import=None, scaling_<wbr>configuration=None, skip_<wbr>final_<wbr>snapshot=None, snapshot_<wbr>identifier=None, source_<wbr>region=None, storage_<wbr>encrypted=None, tags=None, vpc_<wbr>security_<wbr>group_<wbr>ids=None)
```

```go
func GetCluster(ctx *pulumi.Context, name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Cluster Get(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null);
```

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>S3Import<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Username</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">*rds.<wbr>Cluster<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">*rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack<wbr>Window</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Members</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Cluster<wbr>Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion<wbr>Protection</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Http<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>Engine<wbr>Type?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Mode</td>
            <td class="align-top">
                
                <code>Engine<wbr>Mode?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Cluster<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Roles</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reader<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">rds.<wbr>Cluster<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">rds.<wbr>Cluster<wbr>Scaling<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next deployment. It is recommended to specify 3 AZs or use `ignore_changes` if necessary.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backtrack_<wbr>window</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The days to retain backups for. Default `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The cluster identifier. If omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>members</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of RDS Instances that are a part of this cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Cluster Resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy_<wbr>tags_<wbr>to_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy all Cluster `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>cluster_<wbr>parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A cluster parameter group to associate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws.rds.ClusterInstance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deletion_<wbr>protection</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the DB instance should have deletion protection enabled. The database can&#39;t be deleted when this value is set to `true`. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>http_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS address of the RDS instance
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final_<wbr>snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>cluster_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The global cluster identifier specified on [`aws.rds.GlobalCluster`](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Route53 Hosted Zone ID of the endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>database_<wbr>authentication_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>roles</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of ARNs for the IAM roles to associate to the RDS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port on which the DB accepts connections
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reader_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>source_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#clusters3import">dict{cluster_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#clusterscalingconfiguration">dict{cluster_<wbr>scaling_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip_<wbr>final_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source region for an encrypted replica DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the DB cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC security groups to associate
with the Cluster
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClusterS3Import
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterS3Import">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterS3Import">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#ClusterS3ImportArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#ClusterS3ImportOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.ClusterS3ImportArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.ClusterS3Import.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The bucket name where your backup is stored
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be blank, but is the path to your backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingestion<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Role applied to load the data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source engine for the backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Version of the source engine used to make the backup
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The bucket name where your backup is stored
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be blank, but is the path to your backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingestion<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Role applied to load the data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source engine for the backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Version of the source engine used to make the backup
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The bucket name where your backup is stored
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be blank, but is the path to your backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingestion<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Role applied to load the data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source engine for the backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Version of the source engine used to make the backup
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The bucket name where your backup is stored
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be blank, but is the path to your backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingestion_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Role applied to load the data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source engine for the backup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Version of the source engine used to make the backup
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterScalingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterScalingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterScalingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#ClusterScalingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#ClusterScalingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.ClusterScalingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.ClusterScalingConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable automatic pause. A DB cluster can be paused only when it&#39;s idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Seconds<wbr>Until<wbr>Auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable automatic pause. A DB cluster can be paused only when it&#39;s idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Seconds<wbr>Until<wbr>Auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Action</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable automatic pause. A DB cluster can be paused only when it&#39;s idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">seconds<wbr>Until<wbr>Auto<wbr>Pause</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auto_<wbr>pause</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable automatic pause. A DB cluster can be paused only when it&#39;s idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">seconds_<wbr>until_<wbr>auto_<wbr>pause</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







