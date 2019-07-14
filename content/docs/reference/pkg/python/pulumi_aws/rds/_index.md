---
---

<div class="section" id="rds">
<h1>rds<a class="headerlink" href="#rds" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.rds"></span><dl class="class">
<dt id="pulumi_aws.rds.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>apply_immediately=None</em>, <em>availability_zones=None</em>, <em>backtrack_window=None</em>, <em>backup_retention_period=None</em>, <em>cluster_identifier=None</em>, <em>cluster_identifier_prefix=None</em>, <em>cluster_members=None</em>, <em>copy_tags_to_snapshot=None</em>, <em>database_name=None</em>, <em>db_cluster_parameter_group_name=None</em>, <em>db_subnet_group_name=None</em>, <em>deletion_protection=None</em>, <em>enabled_cloudwatch_logs_exports=None</em>, <em>engine=None</em>, <em>engine_mode=None</em>, <em>engine_version=None</em>, <em>final_snapshot_identifier=None</em>, <em>global_cluster_identifier=None</em>, <em>iam_database_authentication_enabled=None</em>, <em>iam_roles=None</em>, <em>kms_key_id=None</em>, <em>master_password=None</em>, <em>master_username=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>replication_source_identifier=None</em>, <em>s3_import=None</em>, <em>scaling_configuration=None</em>, <em>skip_final_snapshot=None</em>, <em>snapshot_identifier=None</em>, <em>source_region=None</em>, <em>storage_encrypted=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Cluster resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html">Amazon RDS Documentation for more information.</a></li>
<li><strong>backtrack_window</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target backtrack window, in seconds. Only available for <code class="docutils literal notranslate"><span class="pre">aurora</span></code> engine currently. To disable backtracking, set this value to <code class="docutils literal notranslate"><span class="pre">0</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>. Must be between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">259200</span></code> (72 hours)</li>
<li><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></li>
<li><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code>.</li>
<li><strong>cluster_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of RDS Instances that are a part of this cluster</li>
<li><strong>copy_tags_to_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Copy all Cluster <code class="docutils literal notranslate"><span class="pre">tags</span></code> to snapshots. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]</li>
<li><strong>db_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</li>
<li><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A DB subnet group to associate with this DB instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">db_subnet_group_name</span></code> specified on every <cite>``aws_rds_cluster_instance`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html</a>&gt;`_ in the cluster.</li>
<li><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the DB instance should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>enabled_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">general</span></code>, <code class="docutils literal notranslate"><span class="pre">slowquery</span></code>.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-mysql</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-postgresql</span></code></li>
<li><strong>engine_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine mode. Valid values: <code class="docutils literal notranslate"><span class="pre">global</span></code>, <code class="docutils literal notranslate"><span class="pre">parallelquery</span></code>, <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>, <code class="docutils literal notranslate"><span class="pre">serverless</span></code>. Defaults to: <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html">RDS User Guide</a> for limitations when using <code class="docutils literal notranslate"><span class="pre">serverless</span></code>.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version. Updating this argument results in an outage. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html">Aurora MySQL</a> and <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html">Aurora Postgres</a> documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is <code class="docutils literal notranslate"><span class="pre">5.7.mysql_aurora.2.03.2</span></code>.</li>
<li><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</li>
<li><strong>global_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The global cluster identifier specified on <cite>``aws_rds_global_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html</a>&gt;`_.</li>
<li><strong>iam_database_authentication_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html">AWS Documentation</a> for availability and limitations.</li>
<li><strong>iam_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of ARNs for the IAM roles to associate to the RDS Cluster.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</li>
<li><strong>master_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]</li>
<li><strong>master_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for the master DB user. Please refer to the [RDS Naming Constraints][5]</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections</li>
<li><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</li>
<li><strong>replication_source_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.</li>
<li><strong>scaling_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested attribute with scaling properties. Only valid when <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">serverless</span></code>. More details below.</li>
<li><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</li>
<li><strong>source_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source region for an encrypted replica DB cluster.</li>
<li><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> for <code class="docutils literal notranslate"><span class="pre">provisioned</span></code> <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">serverless</span></code> <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the DB cluster.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate
with the Cluster</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html">Amazon RDS Documentation for more information.</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.backtrack_window">
<code class="descname">backtrack_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.backtrack_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The target backtrack window, in seconds. Only available for <code class="docutils literal notranslate"><span class="pre">aurora</span></code> engine currently. To disable backtracking, set this value to <code class="docutils literal notranslate"><span class="pre">0</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>. Must be between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">259200</span></code> (72 hours)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.backup_retention_period">
<code class="descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.cluster_identifier_prefix">
<code class="descname">cluster_identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.cluster_identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.cluster_members">
<code class="descname">cluster_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.cluster_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of RDS Instances that are a part of this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.cluster_resource_id">
<code class="descname">cluster_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RDS Cluster Resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.copy_tags_to_snapshot">
<code class="descname">copy_tags_to_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.copy_tags_to_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Copy all Cluster <code class="docutils literal notranslate"><span class="pre">tags</span></code> to snapshots. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.db_cluster_parameter_group_name">
<code class="descname">db_cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.db_cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A cluster parameter group to associate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.db_subnet_group_name">
<code class="descname">db_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A DB subnet group to associate with this DB instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">db_subnet_group_name</span></code> specified on every <cite>``aws_rds_cluster_instance`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html</a>&gt;`_ in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.deletion_protection">
<code class="descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>If the DB instance should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.enabled_cloudwatch_logs_exports">
<code class="descname">enabled_cloudwatch_logs_exports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.enabled_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">general</span></code>, <code class="docutils literal notranslate"><span class="pre">slowquery</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address of the RDS instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-mysql</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-postgresql</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.engine_mode">
<code class="descname">engine_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.engine_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine mode. Valid values: <code class="docutils literal notranslate"><span class="pre">global</span></code>, <code class="docutils literal notranslate"><span class="pre">parallelquery</span></code>, <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>, <code class="docutils literal notranslate"><span class="pre">serverless</span></code>. Defaults to: <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html">RDS User Guide</a> for limitations when using <code class="docutils literal notranslate"><span class="pre">serverless</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version. Updating this argument results in an outage. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html">Aurora MySQL</a> and <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html">Aurora Postgres</a> documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is <code class="docutils literal notranslate"><span class="pre">5.7.mysql_aurora.2.03.2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.final_snapshot_identifier">
<code class="descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.global_cluster_identifier">
<code class="descname">global_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.global_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The global cluster identifier specified on <cite>``aws_rds_global_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route53 Hosted Zone ID of the endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.iam_database_authentication_enabled">
<code class="descname">iam_database_authentication_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.iam_database_authentication_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html">AWS Documentation</a> for availability and limitations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.iam_roles">
<code class="descname">iam_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of ARNs for the IAM roles to associate to the RDS Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.master_password">
<code class="descname">master_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.master_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.master_username">
<code class="descname">master_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the master DB user. Please refer to the [RDS Naming Constraints][5]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.reader_endpoint">
<code class="descname">reader_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.reader_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.replication_source_identifier">
<code class="descname">replication_source_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.replication_source_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.scaling_configuration">
<code class="descname">scaling_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.scaling_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute with scaling properties. Only valid when <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">serverless</span></code>. More details below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.skip_final_snapshot">
<code class="descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.snapshot_identifier">
<code class="descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.source_region">
<code class="descname">source_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.source_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The source region for an encrypted replica DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> for <code class="docutils literal notranslate"><span class="pre">provisioned</span></code> <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">serverless</span></code> <code class="docutils literal notranslate"><span class="pre">engine_mode</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Cluster.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to associate
with the Cluster</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.ClusterEndpoint">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">ClusterEndpoint</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_endpoint_identifier=None</em>, <em>cluster_identifier=None</em>, <em>custom_endpoint_type=None</em>, <em>excluded_members=None</em>, <em>static_members=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RDS Aurora Cluster Endpoint.
You can refer to the [User Guide][1].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_endpoint_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier to use for the new endpoint. This parameter is stored as a lowercase string.</li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier.</li>
<li><strong>custom_endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the endpoint. One of: READER , ANY .</li>
<li><strong>excluded_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DB instance identifiers that aren’t part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with <code class="docutils literal notranslate"><span class="pre">static_members</span></code>.</li>
<li><strong>static_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DB instance identifiers that are part of the custom endpoint group. Conflicts with <code class="docutils literal notranslate"><span class="pre">excluded_members</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_endpoint.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.cluster_endpoint_identifier">
<code class="descname">cluster_endpoint_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.cluster_endpoint_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier to use for the new endpoint. This parameter is stored as a lowercase string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.custom_endpoint_type">
<code class="descname">custom_endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.custom_endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the endpoint. One of: READER , ANY .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom endpoint for the Aurora cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.excluded_members">
<code class="descname">excluded_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.excluded_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DB instance identifiers that aren’t part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with <code class="docutils literal notranslate"><span class="pre">static_members</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterEndpoint.static_members">
<code class="descname">static_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.static_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DB instance identifiers that are part of the custom endpoint group. Conflicts with <code class="docutils literal notranslate"><span class="pre">excluded_members</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterEndpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterEndpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.ClusterInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">ClusterInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>cluster_identifier=None</em>, <em>copy_tags_to_snapshot=None</em>, <em>db_parameter_group_name=None</em>, <em>db_subnet_group_name=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>identifier=None</em>, <em>identifier_prefix=None</em>, <em>instance_class=None</em>, <em>monitoring_interval=None</em>, <em>monitoring_role_arn=None</em>, <em>performance_insights_enabled=None</em>, <em>performance_insights_kms_key_id=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>promotion_tier=None</em>, <em>publicly_accessible=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClusterInstance resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">docs</a> about the details.</li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``aws_rds_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster.html</a>&gt;`_ in which to launch this instance.</li>
<li><strong>copy_tags_to_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to copy all of the user-defined tags from the DB instance to snapshots of the DB instance. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>db_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DB parameter group to associate with this instance.</li>
<li><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A DB subnet group to associate with this DB instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">db_subnet_group_name</span></code> of the attached <cite>``aws_rds_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster.html</a>&gt;`_.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the RDS instance. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-mysql</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-postgresql</span></code>.
For information on the difference between the available Aurora MySQL engines
see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html">Comparison between Aurora MySQL 1 and Aurora MySQL 2</a>
in the Amazon RDS User Guide.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version.</li>
<li><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</li>
<li><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora uses <code class="docutils literal notranslate"><span class="pre">db.*</span></code> instance classes/types. Please see [AWS Documentation][7] for currently available instance classes and complete details.</li>
<li><strong>monitoring_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.</li>
<li><strong>monitoring_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html">AWS Documentation</a>
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.</p>
</li>
<li><strong>performance_insights_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether Performance Insights is enabled or not.</li>
<li><strong>performance_insights_kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS key to encrypt Performance Insights data. When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true.</li>
<li><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled.
Eg: “04:00-09:00”</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</li>
<li><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool to control if instance is publicly accessible.
Default <code class="docutils literal notranslate"><span class="pre">false</span></code>. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">docs</a> about the details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``aws_rds_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster.html</a>&gt;`_ in which to launch this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.copy_tags_to_snapshot">
<code class="descname">copy_tags_to_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.copy_tags_to_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to copy all of the user-defined tags from the DB instance to snapshots of the DB instance. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.db_parameter_group_name">
<code class="descname">db_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.db_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DB parameter group to associate with this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.db_subnet_group_name">
<code class="descname">db_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A DB subnet group to associate with this DB instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">db_subnet_group_name</span></code> of the attached <cite>``aws_rds_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">https://www.terraform.io/docs/providers/aws/r/rds_cluster.html</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.dbi_resource_id">
<code class="descname">dbi_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.dbi_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region-unique, immutable identifier for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address for this instance. May not be writable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for the RDS instance. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-mysql</span></code>, <code class="docutils literal notranslate"><span class="pre">aurora-postgresql</span></code>.
For information on the difference between the available Aurora MySQL engines
see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html">Comparison between Aurora MySQL 1 and Aurora MySQL 2</a>
in the Amazon RDS User Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.identifier_prefix">
<code class="descname">identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.instance_class">
<code class="descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora uses <code class="docutils literal notranslate"><span class="pre">db.*</span></code> instance classes/types. Please see [AWS Documentation][7] for currently available instance classes and complete details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key if one is set to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.monitoring_interval">
<code class="descname">monitoring_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.monitoring_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.monitoring_role_arn">
<code class="descname">monitoring_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.monitoring_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html">AWS Documentation</a>
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.performance_insights_enabled">
<code class="descname">performance_insights_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.performance_insights_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether Performance Insights is enabled or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.performance_insights_kms_key_id">
<code class="descname">performance_insights_kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.performance_insights_kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS key to encrypt Performance Insights data. When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The database port</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled.
Eg: “04:00-09:00”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.promotion_tier">
<code class="descname">promotion_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.promotion_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Bool to control if instance is publicly accessible.
Default <code class="docutils literal notranslate"><span class="pre">false</span></code>. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterInstance.writer">
<code class="descname">writer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.writer" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.ClusterParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS DB cluster parameter group resource. Documentation of the available parameters for various Aurora engines can be found at:</p>
<ul class="simple">
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html">Aurora MySQL Parameters</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html">Aurora PostgreSQL Parameters</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the DB cluster parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DB parameter.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via <cite>``aws rds describe-db-cluster-parameters`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html">https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html</a>&gt;`_ after initial creation of the group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_parameter_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_parameter_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the db cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the DB cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DB parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via <cite>``aws rds describe-db-cluster-parameters`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html">https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html</a>&gt;`_ after initial creation of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.ClusterSnapshot">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">ClusterSnapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>db_cluster_identifier=None</em>, <em>db_cluster_snapshot_identifier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the <cite>``aws_db_snapshot`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/db_snapshot.html">https://www.terraform.io/docs/providers/aws/r/db_snapshot.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB Cluster Identifier from which to take the snapshot.</li>
<li><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_cluster_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_cluster_snapshot.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.db_cluster_identifier">
<code class="descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB Cluster Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.db_cluster_snapshot_arn">
<code class="descname">db_cluster_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.db_cluster_snapshot_identifier">
<code class="descname">db_cluster_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.db_cluster_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ClusterSnapshot.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DB cluster snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterSnapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ClusterSnapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ClusterSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.EventSubscription">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">EventSubscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>event_categories=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>sns_topic=None</em>, <em>source_ids=None</em>, <em>source_type=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DB event subscription resource.</p>
<p>The following additional atttributes are provided:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">id</span></code> - The name of the RDS event notification subscription</li>
<li><code class="docutils literal notranslate"><span class="pre">arn</span></code> - The Amazon Resource Name of the RDS event notification subscription</li>
<li><code class="docutils literal notranslate"><span class="pre">customer_aws_id</span></code> - The AWS customer account associated with the RDS event notification subscription</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable the subscription. Defaults to true.</li>
<li><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event categories for a SourceType that you want to subscribe to. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html">http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html</a> or run <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">rds</span> <span class="pre">describe-event-categories</span></code>.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DB event subscription. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>sns_topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SNS topic to send events to.</li>
<li><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.</li>
<li><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source that will be generating the events. Valid options are <code class="docutils literal notranslate"><span class="pre">db-instance</span></code>, <code class="docutils literal notranslate"><span class="pre">db-security-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-parameter-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-snapshot</span></code>, <code class="docutils literal notranslate"><span class="pre">db-cluster</span></code> or <code class="docutils literal notranslate"><span class="pre">db-cluster-snapshot</span></code>. If not set, all sources will be subscribed to.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_event_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_event_subscription.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable the subscription. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.event_categories">
<code class="descname">event_categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of event categories for a SourceType that you want to subscribe to. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html">http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html</a> or run <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">rds</span> <span class="pre">describe-event-categories</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DB event subscription. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.sns_topic">
<code class="descname">sns_topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.sns_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The SNS topic to send events to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.source_ids">
<code class="descname">source_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.source_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.source_type">
<code class="descname">source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source that will be generating the events. Valid options are <code class="docutils literal notranslate"><span class="pre">db-instance</span></code>, <code class="docutils literal notranslate"><span class="pre">db-security-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-parameter-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-snapshot</span></code>, <code class="docutils literal notranslate"><span class="pre">db-cluster</span></code> or <code class="docutils literal notranslate"><span class="pre">db-cluster-snapshot</span></code>. If not set, all sources will be subscribed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.EventSubscription.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.EventSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.EventSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>availability_zones=None</em>, <em>backup_retention_period=None</em>, <em>cluster_identifier=None</em>, <em>cluster_members=None</em>, <em>cluster_resource_id=None</em>, <em>database_name=None</em>, <em>db_cluster_parameter_group_name=None</em>, <em>db_subnet_group_name=None</em>, <em>enabled_cloudwatch_logs_exports=None</em>, <em>endpoint=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>final_snapshot_identifier=None</em>, <em>hosted_zone_id=None</em>, <em>iam_database_authentication_enabled=None</em>, <em>iam_roles=None</em>, <em>kms_key_id=None</em>, <em>master_username=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>reader_endpoint=None</em>, <em>replication_source_identifier=None</em>, <em>storage_encrypted=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GetClusterSnapshotResult</code><span class="sig-paren">(</span><em>allocated_storage=None</em>, <em>availability_zones=None</em>, <em>db_cluster_identifier=None</em>, <em>db_cluster_snapshot_arn=None</em>, <em>db_cluster_snapshot_identifier=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>include_public=None</em>, <em>include_shared=None</em>, <em>kms_key_id=None</em>, <em>license_model=None</em>, <em>most_recent=None</em>, <em>port=None</em>, <em>snapshot_create_time=None</em>, <em>snapshot_type=None</em>, <em>source_db_cluster_snapshot_arn=None</em>, <em>status=None</em>, <em>storage_encrypted=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusterSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.db_cluster_identifier">
<code class="descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.db_cluster_snapshot_arn">
<code class="descname">db_cluster_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.snapshot_create_time">
<code class="descname">snapshot_create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.snapshot_create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time when the snapshot was taken, in Universal Coordinated Time (UTC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetClusterSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetClusterSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GetEventCategoriesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GetEventCategoriesResult</code><span class="sig-paren">(</span><em>event_categories=None</em>, <em>source_type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GetEventCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEventCategories.</p>
<dl class="attribute">
<dt id="pulumi_aws.rds.GetEventCategoriesResult.event_categories">
<code class="descname">event_categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetEventCategoriesResult.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the event categories.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetEventCategoriesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetEventCategoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GetInstanceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GetInstanceResult</code><span class="sig-paren">(</span><em>address=None</em>, <em>allocated_storage=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>backup_retention_period=None</em>, <em>ca_cert_identifier=None</em>, <em>db_cluster_identifier=None</em>, <em>db_instance_arn=None</em>, <em>db_instance_class=None</em>, <em>db_instance_identifier=None</em>, <em>db_instance_port=None</em>, <em>db_name=None</em>, <em>db_parameter_groups=None</em>, <em>db_security_groups=None</em>, <em>db_subnet_group=None</em>, <em>enabled_cloudwatch_logs_exports=None</em>, <em>endpoint=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>hosted_zone_id=None</em>, <em>iops=None</em>, <em>kms_key_id=None</em>, <em>license_model=None</em>, <em>master_username=None</em>, <em>monitoring_interval=None</em>, <em>monitoring_role_arn=None</em>, <em>multi_az=None</em>, <em>option_group_memberships=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>publicly_accessible=None</em>, <em>replicate_source_db=None</em>, <em>resource_id=None</em>, <em>storage_encrypted=None</em>, <em>storage_type=None</em>, <em>timezone=None</em>, <em>vpc_security_groups=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the RDS instance. See also <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> and <code class="docutils literal notranslate"><span class="pre">port</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size specified in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor version patches are applied automatically.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Availability Zone the DB instance is located in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.backup_retention_period">
<code class="descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days for which automatic DB snapshots are retained.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.ca_cert_identifier">
<code class="descname">ca_cert_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.ca_cert_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier of the CA certificate for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_cluster_identifier">
<code class="descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_instance_arn">
<code class="descname">db_instance_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_instance_class">
<code class="descname">db_instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the name of the compute and memory capacity class of the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_instance_port">
<code class="descname">db_instance_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_instance_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the port that the DB instance listens on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_name">
<code class="descname">db_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_parameter_groups">
<code class="descname">db_parameter_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_parameter_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the list of DB parameter groups applied to this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_security_groups">
<code class="descname">db_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides List of DB security groups associated to this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.db_subnet_group">
<code class="descname">db_subnet_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.db_subnet_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the subnet group associated with the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.enabled_cloudwatch_logs_exports">
<code class="descname">enabled_cloudwatch_logs_exports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.enabled_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of log types to export to cloudwatch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection endpoint in <code class="docutils literal notranslate"><span class="pre">address:port</span></code> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the name of the database engine to be used for this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the database engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Provisioned IOPS (I/O operations per second) value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.master_username">
<code class="descname">master_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the master username for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.monitoring_interval">
<code class="descname">monitoring_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.monitoring_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.monitoring_role_arn">
<code class="descname">monitoring_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.monitoring_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.multi_az">
<code class="descname">multi_az</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.multi_az" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the DB instance is a Multi-AZ deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.option_group_memberships">
<code class="descname">option_group_memberships</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.option_group_memberships" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the list of option group memberships for this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The database port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the daily time range during which automated backups are created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range during which system maintenance can occur in UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the accessibility options for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.replicate_source_db">
<code class="descname">replicate_source_db</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.replicate_source_db" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the source DB that this is a replica of.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RDS Resource ID of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB instance is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage type associated with DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.timezone">
<code class="descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The time zone of the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.vpc_security_groups">
<code class="descname">vpc_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.vpc_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a list of VPC security group elements that the DB instance belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetInstanceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GetSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GetSnapshotResult</code><span class="sig-paren">(</span><em>allocated_storage=None</em>, <em>availability_zone=None</em>, <em>db_instance_identifier=None</em>, <em>db_snapshot_arn=None</em>, <em>db_snapshot_identifier=None</em>, <em>encrypted=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>include_public=None</em>, <em>include_shared=None</em>, <em>iops=None</em>, <em>kms_key_id=None</em>, <em>license_model=None</em>, <em>most_recent=None</em>, <em>option_group_name=None</em>, <em>port=None</em>, <em>snapshot_create_time=None</em>, <em>snapshot_type=None</em>, <em>source_db_snapshot_identifier=None</em>, <em>source_region=None</em>, <em>status=None</em>, <em>storage_type=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.db_snapshot_arn">
<code class="descname">db_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.db_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.option_group_name">
<code class="descname">option_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.option_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the option group name for the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.snapshot_create_time">
<code class="descname">snapshot_create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.snapshot_create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.source_db_snapshot_identifier">
<code class="descname">source_db_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.source_db_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.source_region">
<code class="descname">source_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.source_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region that the DB snapshot was created in or copied from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the status of this DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage type associated with DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the VPC associated with the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GetSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.GlobalCluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">GlobalCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database_name=None</em>, <em>deletion_protection=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>global_cluster_identifier=None</em>, <em>storage_encrypted=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RDS Global Cluster, which is an Aurora global database spread across multiple regions. The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.</p>
<p>More information about Aurora global databases can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database-creating">Aurora User Guide</a>.</p>
<blockquote>
<div><strong>NOTE:</strong> RDS only supports the <code class="docutils literal notranslate"><span class="pre">aurora</span></code> engine (MySQL 5.6 compatible) for Global Clusters at this time.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for an automatically created database on cluster creation.</li>
<li><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the Global Cluster should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database engine to be used for this DB cluster. Valid values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Engine version of the Aurora global database.</li>
<li><strong>global_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The global cluster identifier.</li>
<li><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_global_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_global_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>RDS Global Cluster Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for an automatically created database on cluster creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.deletion_protection">
<code class="descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>If the Global Cluster should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database engine to be used for this DB cluster. Valid values: <code class="docutils literal notranslate"><span class="pre">aurora</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aurora</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Engine version of the Aurora global database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.global_cluster_identifier">
<code class="descname">global_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.global_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The global cluster identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.global_cluster_resource_id">
<code class="descname">global_cluster_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.global_cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Region-unique, immutable identifier for the global database cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.GlobalCluster.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.GlobalCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.GlobalCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.GlobalCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.Instance">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocated_storage=None</em>, <em>allow_major_version_upgrade=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>backup_retention_period=None</em>, <em>backup_window=None</em>, <em>character_set_name=None</em>, <em>copy_tags_to_snapshot=None</em>, <em>db_subnet_group_name=None</em>, <em>deletion_protection=None</em>, <em>domain=None</em>, <em>domain_iam_role_name=None</em>, <em>enabled_cloudwatch_logs_exports=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>final_snapshot_identifier=None</em>, <em>iam_database_authentication_enabled=None</em>, <em>identifier=None</em>, <em>identifier_prefix=None</em>, <em>instance_class=None</em>, <em>iops=None</em>, <em>kms_key_id=None</em>, <em>license_model=None</em>, <em>maintenance_window=None</em>, <em>max_allocated_storage=None</em>, <em>monitoring_interval=None</em>, <em>monitoring_role_arn=None</em>, <em>multi_az=None</em>, <em>name=None</em>, <em>option_group_name=None</em>, <em>parameter_group_name=None</em>, <em>password=None</em>, <em>performance_insights_enabled=None</em>, <em>performance_insights_kms_key_id=None</em>, <em>performance_insights_retention_period=None</em>, <em>port=None</em>, <em>publicly_accessible=None</em>, <em>replicate_source_db=None</em>, <em>s3_import=None</em>, <em>security_group_names=None</em>, <em>skip_final_snapshot=None</em>, <em>snapshot_identifier=None</em>, <em>storage_encrypted=None</em>, <em>storage_type=None</em>, <em>tags=None</em>, <em>timezone=None</em>, <em>username=None</em>, <em>vpc_security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The allocated storage in gibibytes. If <code class="docutils literal notranslate"><span class="pre">max_allocated_storage</span></code> is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.</li>
<li><strong>allow_major_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html">Amazon RDS Documentation for more
information.</a></p>
</li>
<li><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ for the RDS instance.</li>
<li><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Must be
between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">35</span></code>. Must be greater than <code class="docutils literal notranslate"><span class="pre">0</span></code> if the database is used as a source for a Read Replica. [See Read Replica][1].</li>
<li><strong>backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: “09:46-10:16”. Must
not overlap with <code class="docutils literal notranslate"><span class="pre">maintenance_window</span></code>.</li>
<li><strong>character_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The character set name to use for DB
encoding in Oracle instances. This can’t be changed. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html">Oracle Character Sets
Supported in Amazon
RDS</a>
for more information.</li>
<li><strong>copy_tags_to_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Copy all Instance <code class="docutils literal notranslate"><span class="pre">tags</span></code> to snapshots. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html">DB subnet group</a>. DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the <code class="docutils literal notranslate"><span class="pre">default</span></code> VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html">DBSubnetGroupName in API
action CreateDBInstanceReadReplica</a>
for additional read replica contraints.</li>
<li><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the DB instance should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Directory Service Active Directory domain to create the instance in.</li>
<li><strong>domain_iam_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM role to be used when making API calls to the Directory Service.</li>
<li><strong>enabled_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on <code class="docutils literal notranslate"><span class="pre">engine</span></code>): <code class="docutils literal notranslate"><span class="pre">alert</span></code>, <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">general</span></code>, <code class="docutils literal notranslate"><span class="pre">listener</span></code>, <code class="docutils literal notranslate"><span class="pre">slowquery</span></code>, <code class="docutils literal notranslate"><span class="pre">trace</span></code>, <code class="docutils literal notranslate"><span class="pre">postgresql</span></code> (PostgreSQL), <code class="docutils literal notranslate"><span class="pre">upgrade</span></code> (PostgreSQL).</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) The database engine to use.  For supported values, see the Engine parameter in <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">API action CreateDBInstance</a>.
Note that for Amazon Aurora instances the engine must match the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">DB cluster</a>’s engine’.
For information on the difference between the available Aurora MySQL engines
see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html">Comparison between Aurora MySQL 1 and Aurora MySQL 2</a>
in the Amazon RDS User Guide.</p>
</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The engine version to use. If <code class="docutils literal notranslate"><span class="pre">auto_minor_version_upgrade</span></code>
is enabled, you can provide a prefix of the version such as <code class="docutils literal notranslate"><span class="pre">5.7</span></code> (for <code class="docutils literal notranslate"><span class="pre">5.7.10</span></code>) and
this attribute will ignore differences in the patch version automatically (e.g. <code class="docutils literal notranslate"><span class="pre">5.7.17</span></code>).
For supported values, see the EngineVersion parameter in <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">API action CreateDBInstance</a>.
Note that for Amazon Aurora instances the engine version must match the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">DB cluster</a>’s engine version’.</p>
</li>
<li><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.</li>
<li><strong>iam_database_authentication_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.</li>
<li><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique
identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</li>
<li><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance type of the RDS instance.</li>
<li><strong>iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of provisioned IOPS. Setting this implies a
storage_type of “io1”.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.</li>
<li><strong>license_model</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.</li>
<li><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow">RDS
Maintenance Window
docs</a>
for more information.</li>
<li><strong>max_allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to <code class="docutils literal notranslate"><span class="pre">allocated_storage</span></code>. Must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">allocated_storage</span></code> or <code class="docutils literal notranslate"><span class="pre">0</span></code> to disable Storage Autoscaling.</li>
<li><strong>monitoring_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.</li>
<li><strong>monitoring_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html">AWS
Documentation</a>
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.</p>
</li>
<li><strong>multi_az</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the RDS instance is multi-AZ</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the <a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html">AWS documentation</a> for more details on what applies for those engines.</p>
</li>
<li><strong>option_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DB option group to associate.</li>
<li><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DB parameter group to
associate.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.</li>
<li><strong>performance_insights_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether Performance Insights are enabled. Defaults to false.</li>
<li><strong>performance_insights_kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS key to encrypt Performance Insights data. When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true. Once KMS key is set, it can never be changed.</li>
<li><strong>performance_insights_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_retention_period</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true. Defaults to ‘7’.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections.</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool to control if instance is publicly
accessible. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>replicate_source_db</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
<code class="docutils literal notranslate"><span class="pre">identifier</span></code> of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>. See [DB Instance Replication][1] and <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html">Working with
PostgreSQL and MySQL Read Replicas</a>
for more information on using Replication.</li>
<li><strong>s3_import</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Restore from a Percona Xtrabackup in S3.  See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html">Importing Data into an Amazon RDS MySQL DB Instance</a></li>
<li><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DB Security Groups to
associate. Only used for <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC">DB Instances on the *EC2-Classic*
Platform</a>.</li>
<li><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you’d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.</li>
<li><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> with a valid ARN. The
default is <code class="docutils literal notranslate"><span class="pre">false</span></code> if not specified.</li>
<li><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of “standard” (magnetic), “gp2” (general
purpose SSD), or “io1” (provisioned IOPS SSD). The default is “io1” if <code class="docutils literal notranslate"><span class="pre">iops</span></code> is
specified, “gp2” if not.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time zone of the DB instance. <code class="docutils literal notranslate"><span class="pre">timezone</span></code> is currently
only supported by Microsoft SQL Server. The <code class="docutils literal notranslate"><span class="pre">timezone</span></code> can only be set on
creation. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone">MSSQL User
Guide</a>
for more information.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) Username for the master DB user.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to
associate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the RDS instance. See also <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> and <code class="docutils literal notranslate"><span class="pre">port</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocated storage in gibibytes. If <code class="docutils literal notranslate"><span class="pre">max_allocated_storage</span></code> is configured, this argument represents the initial storage allocation and differences from the configuration will be ignored automatically when Storage Autoscaling occurs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.allow_major_version_upgrade">
<code class="descname">allow_major_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.allow_major_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html">Amazon RDS Documentation for more
information.</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the RDS instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ for the RDS instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.backup_retention_period">
<code class="descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Must be
between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">35</span></code>. Must be greater than <code class="docutils literal notranslate"><span class="pre">0</span></code> if the database is used as a source for a Read Replica. [See Read Replica][1].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.backup_window">
<code class="descname">backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: “09:46-10:16”. Must
not overlap with <code class="docutils literal notranslate"><span class="pre">maintenance_window</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.ca_cert_identifier">
<code class="descname">ca_cert_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.ca_cert_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier of the CA certificate for the
DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.character_set_name">
<code class="descname">character_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.character_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The character set name to use for DB
encoding in Oracle instances. This can’t be changed. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html">Oracle Character Sets
Supported in Amazon
RDS</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.copy_tags_to_snapshot">
<code class="descname">copy_tags_to_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.copy_tags_to_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Copy all Instance <code class="docutils literal notranslate"><span class="pre">tags</span></code> to snapshots. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.db_subnet_group_name">
<code class="descname">db_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html">DB subnet group</a>. DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the <code class="docutils literal notranslate"><span class="pre">default</span></code> VPC, or in EC2 Classic, if available. When working
with read replicas, it should be specified only if the source database
specifies an instance in another AWS Region. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html">DBSubnetGroupName in API
action CreateDBInstanceReadReplica</a>
for additional read replica contraints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.deletion_protection">
<code class="descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>If the DB instance should have deletion protection enabled. The database can’t be deleted when this value is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Directory Service Active Directory domain to create the instance in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.domain_iam_role_name">
<code class="descname">domain_iam_role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.domain_iam_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM role to be used when making API calls to the Directory Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.enabled_cloudwatch_logs_exports">
<code class="descname">enabled_cloudwatch_logs_exports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.enabled_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be exported. Valid values (depending on <code class="docutils literal notranslate"><span class="pre">engine</span></code>): <code class="docutils literal notranslate"><span class="pre">alert</span></code>, <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">general</span></code>, <code class="docutils literal notranslate"><span class="pre">listener</span></code>, <code class="docutils literal notranslate"><span class="pre">slowquery</span></code>, <code class="docutils literal notranslate"><span class="pre">trace</span></code>, <code class="docutils literal notranslate"><span class="pre">postgresql</span></code> (PostgreSQL), <code class="docutils literal notranslate"><span class="pre">upgrade</span></code> (PostgreSQL).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection endpoint in <code class="docutils literal notranslate"><span class="pre">address:port</span></code> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>(Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) The database engine to use.  For supported values, see the Engine parameter in <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">API action CreateDBInstance</a>.
Note that for Amazon Aurora instances the engine must match the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">DB cluster</a>’s engine’.
For information on the difference between the available Aurora MySQL engines
see <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html">Comparison between Aurora MySQL 1 and Aurora MySQL 2</a>
in the Amazon RDS User Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The engine version to use. If <code class="docutils literal notranslate"><span class="pre">auto_minor_version_upgrade</span></code>
is enabled, you can provide a prefix of the version such as <code class="docutils literal notranslate"><span class="pre">5.7</span></code> (for <code class="docutils literal notranslate"><span class="pre">5.7.10</span></code>) and
this attribute will ignore differences in the patch version automatically (e.g. <code class="docutils literal notranslate"><span class="pre">5.7.17</span></code>).
For supported values, see the EngineVersion parameter in <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html">API action CreateDBInstance</a>.
Note that for Amazon Aurora instances the engine version must match the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/rds_cluster.html">DB cluster</a>’s engine version’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.final_snapshot_identifier">
<code class="descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.iam_database_authentication_enabled">
<code class="descname">iam_database_authentication_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.iam_database_authentication_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.identifier_prefix">
<code class="descname">identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique
identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.instance_class">
<code class="descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of the RDS instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of provisioned IOPS. Setting this implies a
storage_type of “io1”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.maintenance_window">
<code class="descname">maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow">RDS
Maintenance Window
docs</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.max_allocated_storage">
<code class="descname">max_allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.max_allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>When configured, the upper limit to which Amazon RDS can automatically scale the storage of the DB instance. Configuring this will automatically ignore differences to <code class="docutils literal notranslate"><span class="pre">allocated_storage</span></code>. Must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">allocated_storage</span></code> or <code class="docutils literal notranslate"><span class="pre">0</span></code> to disable Storage Autoscaling.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.monitoring_interval">
<code class="descname">monitoring_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.monitoring_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.monitoring_role_arn">
<code class="descname">monitoring_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.monitoring_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html">AWS
Documentation</a>
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.multi_az">
<code class="descname">multi_az</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.multi_az" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the RDS instance is multi-AZ</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the <a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html">AWS documentation</a> for more details on what applies for those engines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.option_group_name">
<code class="descname">option_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.option_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DB option group to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.parameter_group_name">
<code class="descname">parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DB parameter group to
associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.password" title="Permalink to this definition">¶</a></dt>
<dd><p>(Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.performance_insights_enabled">
<code class="descname">performance_insights_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.performance_insights_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether Performance Insights are enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.performance_insights_kms_key_id">
<code class="descname">performance_insights_kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.performance_insights_kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS key to encrypt Performance Insights data. When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true. Once KMS key is set, it can never be changed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.performance_insights_retention_period">
<code class="descname">performance_insights_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.performance_insights_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731 (2 years). When specifying <code class="docutils literal notranslate"><span class="pre">performance_insights_retention_period</span></code>, <code class="docutils literal notranslate"><span class="pre">performance_insights_enabled</span></code> needs to be set to true. Defaults to ‘7’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Bool to control if instance is publicly
accessible. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.replicate_source_db">
<code class="descname">replicate_source_db</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.replicate_source_db" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
<code class="docutils literal notranslate"><span class="pre">identifier</span></code> of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>. See [DB Instance Replication][1] and <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html">Working with
PostgreSQL and MySQL Read Replicas</a>
for more information on using Replication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RDS Resource ID of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.s3_import">
<code class="descname">s3_import</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.s3_import" title="Permalink to this definition">¶</a></dt>
<dd><p>Restore from a Percona Xtrabackup in S3.  See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html">Importing Data into an Amazon RDS MySQL DB Instance</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.security_group_names">
<code class="descname">security_group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DB Security Groups to
associate. Only used for <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC">DB Instances on the *EC2-Classic*
Platform</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.skip_final_snapshot">
<code class="descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.snapshot_identifier">
<code class="descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you’d find in the
RDS console, e.g: rds:production-2015-06-26-06-05.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The RDS instance status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> with a valid ARN. The
default is <code class="docutils literal notranslate"><span class="pre">false</span></code> if not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>One of “standard” (magnetic), “gp2” (general
purpose SSD), or “io1” (provisioned IOPS SSD). The default is “io1” if <code class="docutils literal notranslate"><span class="pre">iops</span></code> is
specified, “gp2” if not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.timezone">
<code class="descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Time zone of the DB instance. <code class="docutils literal notranslate"><span class="pre">timezone</span></code> is currently
only supported by Microsoft SQL Server. The <code class="docutils literal notranslate"><span class="pre">timezone</span></code> can only be set on
creation. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone">MSSQL User
Guide</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.username" title="Permalink to this definition">¶</a></dt>
<dd><p>(Required unless a <code class="docutils literal notranslate"><span class="pre">snapshot_identifier</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate_source_db</span></code>
is provided) Username for the master DB user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Instance.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Instance.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to
associate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.OptionGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">OptionGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>engine_name=None</em>, <em>major_engine_version=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>options=None</em>, <em>option_group_description=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.OptionGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:</p>
<ul class="simple">
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html">MariaDB Options</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html">Microsoft SQL Server Options</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html">MySQL Options</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html">Oracle Options</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>engine_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the engine that this option group should be associated with.</li>
<li><strong>major_engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the major version of the engine that this option group should be associated with.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the setting.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>. Must be lowercase, to match as it is stored in AWS.</li>
<li><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Options to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_option_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_option_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the db option group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.engine_name">
<code class="descname">engine_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.engine_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the engine that this option group should be associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.major_engine_version">
<code class="descname">major_engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.major_engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the major version of the engine that this option group should be associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the setting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>. Must be lowercase, to match as it is stored in AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.options">
<code class="descname">options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.options" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Options to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.OptionGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.OptionGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.OptionGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.OptionGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.ParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">ParameterGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS DB parameter group resource .Documentation of the available parameters for various RDS engines can be found at:</p>
<ul class="simple">
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html">Aurora MySQL Parameters</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html">Aurora PostgreSQL Parameters</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Parameters.html">MariaDB Parameters</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Oracle.html#USER_ModifyInstance.Oracle.sqlnet">Oracle Parameters</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Parameters">PostgreSQL Parameters</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the DB parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DB parameter.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via <cite>``aws rds describe-db-parameters`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html">https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html</a>&gt;`_ after initial creation of the group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_parameter_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_parameter_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the db parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the DB parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DB parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via <cite>``aws rds describe-db-parameters`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html">https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html</a>&gt;`_ after initial creation of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.ParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.ParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.RoleAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">RoleAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>db_instance_identifier=None</em>, <em>feature_name=None</em>, <em>role_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RDS DB Instance association with an IAM Role. Example use cases:</p>
<ul class="simple">
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html">Amazon RDS Oracle integration with Amazon S3</a></li>
<li><a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html">Importing Amazon S3 Data into an RDS PostgreSQL DB Instance</a></li>
</ul>
<blockquote>
<div>To manage the RDS DB Instance IAM Role for <a class="reference external" href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html">Enhanced Monitoring</a>, see the <code class="docutils literal notranslate"><span class="pre">aws_db_instance</span></code> resource <code class="docutils literal notranslate"><span class="pre">monitoring_role_arn</span></code> argument instead.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>db_instance_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DB Instance Identifier to associate with the IAM Role.</li>
<li><strong>feature_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the feature for association. This can be found in the AWS documentation relevant to the integration or a full list is available in the <code class="docutils literal notranslate"><span class="pre">SupportedFeatureNames</span></code> list returned by <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html">AWS CLI rds describe-db-engine-versions</a>.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_instance_role_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_instance_role_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.RoleAssociation.db_instance_identifier">
<code class="descname">db_instance_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation.db_instance_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>DB Instance Identifier to associate with the IAM Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.RoleAssociation.feature_name">
<code class="descname">feature_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation.feature_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the feature for association. This can be found in the AWS documentation relevant to the integration or a full list is available in the <code class="docutils literal notranslate"><span class="pre">SupportedFeatureNames</span></code> list returned by <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html">AWS CLI rds describe-db-engine-versions</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.RoleAssociation.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.RoleAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.RoleAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.RoleAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.SecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">SecurityGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>ingress=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS security group resource. This is only for DB instances in the
EC2-Classic Platform. For instances inside a VPC, use the
<cite>``aws_db_instance.vpc_security_group_ids`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/db_instance.html#vpc_security_group_ids">https://www.terraform.io/docs/providers/aws/r/db_instance.html#vpc_security_group_ids</a>&gt;`_
attribute instead.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ingress rules.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DB security group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_security_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.SecurityGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The arn of the DB security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SecurityGroup.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ingress rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SecurityGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DB security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SecurityGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.SecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.SecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.Snapshot">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">Snapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>db_instance_identifier=None</em>, <em>db_snapshot_identifier=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RDS database instance snapshot. For managing RDS database cluster snapshots, see the <cite>``aws_db_cluster_snapshot`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/db_cluster_snapshot.html">https://www.terraform.io/docs/providers/aws/r/db_cluster_snapshot.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>db_instance_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB Instance Identifier from which to take the snapshot.</li>
<li><strong>db_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_snapshot.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.db_instance_identifier">
<code class="descname">db_instance_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.db_instance_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB Instance Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.db_snapshot_arn">
<code class="descname">db_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.db_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.db_snapshot_identifier">
<code class="descname">db_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.db_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.option_group_name">
<code class="descname">option_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.option_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the option group name for the DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.source_db_snapshot_identifier">
<code class="descname">source_db_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.source_db_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.source_region">
<code class="descname">source_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.source_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region that the DB snapshot was created in or copied from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the status of this DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage type associated with DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.Snapshot.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.Snapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage type associated with DB snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Snapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.Snapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.rds.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.rds.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS DB subnet group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_subnet_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_subnet_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.rds.SubnetGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the db subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SubnetGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.rds.SubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.rds.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.rds.get_cluster">
<code class="descclassname">pulumi_aws.rds.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>cluster_identifier=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a RDS cluster.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/rds_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/rds_cluster.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.rds.get_cluster_snapshot">
<code class="descclassname">pulumi_aws.rds.</code><code class="descname">get_cluster_snapshot</code><span class="sig-paren">(</span><em>db_cluster_identifier=None</em>, <em>db_cluster_snapshot_identifier=None</em>, <em>include_public=None</em>, <em>include_shared=None</em>, <em>most_recent=None</em>, <em>snapshot_type=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.get_cluster_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a DB Cluster Snapshot for use when provisioning DB clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This data source does not apply to snapshots created on DB Instances. 
See the <cite>``aws_db_snapshot`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/db_snapshot.html">https://www.terraform.io/docs/providers/aws/d/db_snapshot.html</a>&gt;`_ for DB Instance snapshots.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_cluster_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_cluster_snapshot.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.rds.get_instance">
<code class="descclassname">pulumi_aws.rds.</code><code class="descname">get_instance</code><span class="sig-paren">(</span><em>db_instance_identifier=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an RDS instance</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_instance.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.rds.get_snapshot">
<code class="descclassname">pulumi_aws.rds.</code><code class="descname">get_snapshot</code><span class="sig-paren">(</span><em>db_instance_identifier=None</em>, <em>db_snapshot_identifier=None</em>, <em>include_public=None</em>, <em>include_shared=None</em>, <em>most_recent=None</em>, <em>snapshot_type=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.rds.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a DB Snapshot for use when provisioning DB instances</p>
<blockquote>
<div><p><strong>NOTE:</strong> This data source does not apply to snapshots created on Aurora DB clusters.
See the <cite>``aws_db_cluster_snapshot`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/db_cluster_snapshot.html">https://www.terraform.io/docs/providers/aws/d/db_cluster_snapshot.html</a>&gt;`_ for DB Cluster snapshots.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_snapshot.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
