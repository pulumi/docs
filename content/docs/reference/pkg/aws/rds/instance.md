
---
title: "Instance"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an RDS instance resource.  A DB instance is an isolated database
environment in the cloud.  A DB instance can contain multiple user-created
databases.

Changes to a DB instance can occur when you manually change a parameter, such as
`allocated_storage`, and are reflected in the next maintenance window. Because
of this, this provider may report a difference in its planning phase because a
modification has not yet taken place. You can use the `apply_immediately` flag
to instruct the service to apply the change immediately (see documentation
below).

When upgrading the major version of an engine, `allow_major_version_upgrade`
must be set to `true`.

> **Note:** using `apply_immediately` can result in a brief downtime as the
server reboots. See the AWS Docs on [RDS Maintenance][2] for more information.

> **Note:** All arguments including the username and password will be stored in
the raw state as plain-text. [Read more about sensitive data in
state](https://www.terraform.io/docs/state/sensitive-data.html).

## RDS Instance Class Types

Amazon RDS supports three types of instance classes: Standard, Memory Optimized,
and Burstable Performance. For more information please read the AWS RDS documentation
about [DB Instance Class Types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)

## Example Usage

### Basic Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const defaultInstance = new aws.rds.Instance("default", {
    allocatedStorage: 20,
    engine: "mysql",
    engineVersion: "5.7",
    instanceClass: "db.t2.micro",
    name: "mydb",
    parameterGroupName: "default.mysql5.7",
    password: "foobarbaz",
    storageType: "gp2",
    username: "foo",
});
```

### Storage Autoscaling

To enable Storage Autoscaling with instances that support the feature, define the `max_allocated_storage` argument higher than the `allocated_storage` argument. This provider will automatically hide differences with the `allocated_storage` argument value if autoscaling occurs.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.rds.Instance("example", {
    allocatedStorage: 50,
    maxAllocatedStorage: 100,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_instance.html.markdown.



## Create a Instance Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#Instance">Instance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Instance</span><span class="p">(resource_name, id, opts=None, </span>allocated_storage=None<span class="p">, </span>allow_major_version_upgrade=None<span class="p">, </span>apply_immediately=None<span class="p">, </span>auto_minor_version_upgrade=None<span class="p">, </span>availability_zone=None<span class="p">, </span>backup_retention_period=None<span class="p">, </span>backup_window=None<span class="p">, </span>ca_cert_identifier=None<span class="p">, </span>character_set_name=None<span class="p">, </span>copy_tags_to_snapshot=None<span class="p">, </span>db_subnet_group_name=None<span class="p">, </span>delete_automated_backups=None<span class="p">, </span>deletion_protection=None<span class="p">, </span>domain=None<span class="p">, </span>domain_iam_role_name=None<span class="p">, </span>enabled_cloudwatch_logs_exports=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>final_snapshot_identifier=None<span class="p">, </span>iam_database_authentication_enabled=None<span class="p">, </span>identifier=None<span class="p">, </span>identifier_prefix=None<span class="p">, </span>instance_class=None<span class="p">, </span>iops=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>license_model=None<span class="p">, </span>maintenance_window=None<span class="p">, </span>max_allocated_storage=None<span class="p">, </span>monitoring_interval=None<span class="p">, </span>monitoring_role_arn=None<span class="p">, </span>multi_az=None<span class="p">, </span>name=None<span class="p">, </span>option_group_name=None<span class="p">, </span>parameter_group_name=None<span class="p">, </span>password=None<span class="p">, </span>performance_insights_enabled=None<span class="p">, </span>performance_insights_kms_key_id=None<span class="p">, </span>performance_insights_retention_period=None<span class="p">, </span>port=None<span class="p">, </span>publicly_accessible=None<span class="p">, </span>replicate_source_db=None<span class="p">, </span>s3_import=None<span class="p">, </span>security_group_names=None<span class="p">, </span>skip_final_snapshot=None<span class="p">, </span>snapshot_identifier=None<span class="p">, </span>storage_encrypted=None<span class="p">, </span>storage_type=None<span class="p">, </span>tags=None<span class="p">, </span>timezone=None<span class="p">, </span>username=None<span class="p">, </span>vpc_security_group_ids=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.Instance.html">Instance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.InstanceArgs.html">InstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Instance resource with the given unique name, arguments, and options.

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
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Instance<wbr>S3Import<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">*rds.<wbr>Instance<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string | Instance<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Model</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi<wbr>Az</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">rds.<wbr>Instance<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string | Storage<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>major_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca_<wbr>cert_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete_<wbr>automated_<wbr>backups</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>iam_<wbr>role_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>class</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>model</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi_<wbr>az</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate_<wbr>source_<wbr>db</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">dict{instance_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>type</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Instance Output Properties

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
            <td class="align-top">Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AZ for the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Instance `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the IAM role to be used when making API calls to the Directory Service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The connection endpoint in `address:port` format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicas</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Instance<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS instance status.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to
associate.
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
            <td class="align-top">Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AZ for the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Instance `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the IAM role to be used when making API calls to the Directory Service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The connection endpoint in `address:port` format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicas</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">*rds.<wbr>Instance<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}} Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS instance status.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to
associate.
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
            <td class="align-top">address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AZ for the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy<wbr>Tags<wbr>To<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Instance `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db<wbr>Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the IAM role to be used when making API calls to the Directory Service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The connection endpoint in `address:port` format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final<wbr>Snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Database<wbr>Authentication<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Model</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi<wbr>Az</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicas</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">rds.<wbr>Instance<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip<wbr>Final<wbr>Snapshot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RDS instance status.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to
associate.
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
            <td class="align-top">address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>major_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AZ for the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca_<wbr>cert_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy_<wbr>tags_<wbr>to_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Copy all Instance `tags` to snapshots. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">db_<wbr>subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete_<wbr>automated_<wbr>backups</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>iam_<wbr>role_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the IAM role to be used when making API calls to the Directory Service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The connection endpoint in `address:port` format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">final_<wbr>snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of your final DB snapshot
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>database_<wbr>authentication_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>model</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi_<wbr>az</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicas</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate_<wbr>source_<wbr>db</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">dict{instance_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}} Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skip_<wbr>final_<wbr>snapshot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RDS instance status.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of VPC security groups to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Instance Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance;
```

```python
def get(resource_name, id, opts=None, address=None, allocated_<wbr>storage=None, allow_<wbr>major_<wbr>version_<wbr>upgrade=None, apply_<wbr>immediately=None, arn=None, auto_<wbr>minor_<wbr>version_<wbr>upgrade=None, availability_<wbr>zone=None, backup_<wbr>retention_<wbr>period=None, backup_<wbr>window=None, ca_<wbr>cert_<wbr>identifier=None, character_<wbr>set_<wbr>name=None, copy_<wbr>tags_<wbr>to_<wbr>snapshot=None, db_<wbr>subnet_<wbr>group_<wbr>name=None, delete_<wbr>automated_<wbr>backups=None, deletion_<wbr>protection=None, domain=None, domain_<wbr>iam_<wbr>role_<wbr>name=None, enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports=None, endpoint=None, engine=None, engine_<wbr>version=None, final_<wbr>snapshot_<wbr>identifier=None, hosted_<wbr>zone_<wbr>id=None, iam_<wbr>database_<wbr>authentication_<wbr>enabled=None, identifier=None, identifier_<wbr>prefix=None, instance_<wbr>class=None, iops=None, kms_<wbr>key_<wbr>id=None, license_<wbr>model=None, maintenance_<wbr>window=None, max_<wbr>allocated_<wbr>storage=None, monitoring_<wbr>interval=None, monitoring_<wbr>role_<wbr>arn=None, multi_<wbr>az=None, name=None, option_<wbr>group_<wbr>name=None, parameter_<wbr>group_<wbr>name=None, password=None, performance_<wbr>insights_<wbr>enabled=None, performance_<wbr>insights_<wbr>kms_<wbr>key_<wbr>id=None, performance_<wbr>insights_<wbr>retention_<wbr>period=None, port=None, publicly_<wbr>accessible=None, replicas=None, replicate_<wbr>source_<wbr>db=None, resource_<wbr>id=None, s3_<wbr>import=None, security_<wbr>group_<wbr>names=None, skip_<wbr>final_<wbr>snapshot=None, snapshot_<wbr>identifier=None, status=None, storage_<wbr>encrypted=None, storage_<wbr>type=None, tags=None, timezone=None, username=None, vpc_<wbr>security_<wbr>group_<wbr>ids=None)
```

```go
func GetInstance(ctx *pulumi.Context, name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null);
```

Get an existing Instance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
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
The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
The connection endpoint in `address:port` format.
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicas</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">Pulumi.<wbr>Aws.<wbr>Rds.<wbr>Instance<wbr>S3Import<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS instance status.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
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
The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Backup<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
The connection endpoint in `address:port` format.
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Class</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Model</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multi<wbr>Az</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicas</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">*rds.<wbr>Instance<wbr>S3Import</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS instance status.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Type</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timezone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Major<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
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
The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca<wbr>Cert<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete<wbr>Automated<wbr>Backups</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Iam<wbr>Role<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
The connection endpoint in `address:port` format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Class</td>
            <td class="align-top">
                
                <code>string | Instance<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Model</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Allocated<wbr>Storage</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi<wbr>Az</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Insights<wbr>Retention<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicas</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate<wbr>Source<wbr>Db</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">rds.<wbr>Instance<wbr>S3Import?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS instance status.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Type</td>
            <td class="align-top">
                
                <code>string | Storage<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
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
            <td class="align-top">address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname of the RDS instance. See also `endpoint` and `port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The allocated storage in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>major_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
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
The ARN of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AZ for the RDS instance.
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
The days to retain backups for. Must be
between `0` and `35`. Must be greater than `0` if the database is used as a source for a Read Replica. [See Read Replica][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">backup_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: &#34;09:46-10:16&#34;. Must
not overlap with `maintenance_window`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ca_<wbr>cert_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the CA certificate for the DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">character_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The character set name to use for DB
encoding in Oracle instances. This can&#39;t be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.
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
Copy all Instance `tags` to snapshots. Default is `false`.
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
Name of [DB subnet group](https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additional read replica contraints.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete_<wbr>automated_<wbr>backups</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to remove automated backups immediately after the DB instance is deleted. Default is `true`.
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Directory Service Active Directory domain to create the instance in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>iam_<wbr>role_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the IAM role to be used when making API calls to the Directory Service.
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
List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on `engine`): `agent` (MSSQL), `alert`, `audit`, `error`, `general`, `listener`, `slowquery`, `trace`, `postgresql` (PostgreSQL), `upgrade` (PostgreSQL).
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
The connection endpoint in `address:port` format.
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
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine&#39;.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.
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
The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html)&#39;s engine version&#39;.
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
when this DB instance is deleted. Must be provided if `skip_final_snapshot` is
set to `false`.
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
The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).
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
Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the RDS instance,
if omitted, this provider will assign a random, unique identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identifier_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>class</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The instance type of the RDS instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of provisioned IOPS. Setting this implies a
storage_type of &#34;io1&#34;.
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
The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>model</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The window to perform maintenance in.
Syntax: &#34;ddd:hh24:mi-ddd:hh24:mi&#34;. Eg: &#34;Mon:00:00-Mon:03:00&#34;. See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>allocated_<wbr>storage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. Must be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multi_<wbr>az</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies if the RDS instance is multi-AZ
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">option_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB option group to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the DB parameter group to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Performance Insights are enabled. Defaults to false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set, it can never be changed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>insights_<wbr>retention_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` needs to be set to true. Defaults to &#39;7&#39;.
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
The port on which the DB accepts connections.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Bool to control if instance is publicly
accessible. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicas</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replicate_<wbr>source_<wbr>db</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS Resource ID of this instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>import</td>
            <td class="align-top">
                
                <code><a href="#instances3import">dict{instance_<wbr>s3_<wbr>import}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).
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
Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.
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
Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you&#39;d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RDS instance status.
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
Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>type</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One of &#34;standard&#34; (magnetic), &#34;gp2&#34; (general
purpose SSD), or &#34;io1&#34; (provisioned IOPS SSD). The default is &#34;io1&#34; if `iops` is
specified, &#34;gp2&#34; if not.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timezone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.
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
List of VPC security groups to
associate.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### InstanceS3Import
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#InstanceS3Import">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#InstanceS3Import">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#InstanceS3ImportArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#InstanceS3ImportOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.InstanceS3ImportArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.InstanceS3Import.html">output</a> API doc for this type.
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







