---
---

<div class="section" id="module-pulumi_aws.docdb">
<span id="docdb"></span><h1>docdb<a class="headerlink" href="#module-pulumi_aws.docdb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.docdb.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>apply_immediately=None</em>, <em>availability_zones=None</em>, <em>backup_retention_period=None</em>, <em>cluster_identifier=None</em>, <em>cluster_identifier_prefix=None</em>, <em>cluster_members=None</em>, <em>db_cluster_parameter_group_name=None</em>, <em>db_subnet_group_name=None</em>, <em>enabled_cloudwatch_logs_exports=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>final_snapshot_identifier=None</em>, <em>kms_key_id=None</em>, <em>master_password=None</em>, <em>master_username=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>skip_final_snapshot=None</em>, <em>snapshot_identifier=None</em>, <em>storage_encrypted=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster" title="Permalink to this definition">¶</a></dt>
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
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that
instances in the DB cluster can be created in.</li>
<li><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></li>
<li><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifer</span></code>.</li>
<li><strong>cluster_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DocDB Instances that are a part of this cluster</li>
<li><strong>db_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</li>
<li><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A DB subnet group to associate with this DB instance.</li>
<li><strong>enabled_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code></li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version. Updating this argument results in an outage.</li>
<li><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</li>
<li><strong>master_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.</li>
<li><strong>master_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for the master DB user.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections</li>
<li><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</li>
<li><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</li>
<li><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the DB cluster.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate
with the Cluster</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EC2 Availability Zones that
instances in the DB cluster can be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.backup_retention_period">
<code class="descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_identifier_prefix">
<code class="descname">cluster_identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifer</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_members">
<code class="descname">cluster_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DocDB Instances that are a part of this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_resource_id">
<code class="descname">cluster_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DocDB Cluster Resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.db_cluster_parameter_group_name">
<code class="descname">db_cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.db_cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A cluster parameter group to associate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.db_subnet_group_name">
<code class="descname">db_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A DB subnet group to associate with this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.enabled_cloudwatch_logs_exports">
<code class="descname">enabled_cloudwatch_logs_exports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.enabled_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address of the DocDB instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version. Updating this argument results in an outage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.final_snapshot_identifier">
<code class="descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route53 Hosted Zone ID of the endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.master_password">
<code class="descname">master_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.master_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.master_username">
<code class="descname">master_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the master DB user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.reader_endpoint">
<code class="descname">reader_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.reader_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.skip_final_snapshot">
<code class="descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.snapshot_identifier">
<code class="descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.Cluster.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to associate
with the Cluster</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">ClusterInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>cluster_identifier=None</em>, <em>engine=None</em>, <em>identifier=None</em>, <em>identifier_prefix=None</em>, <em>instance_class=None</em>, <em>preferred_maintenance_window=None</em>, <em>promotion_tier=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an DocDB Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [DocDB Cluster][1].</p>
<p>You do not designate a primary and subsequent replicas. Instead, you simply add DocDB
Instances and DocDB manages the replication. You can use the [count][3]
meta-parameter to make multiple instances and join them all to the same DocDB
Cluster, or you may specify different Cluster Instance resources with various
<code class="docutils literal notranslate"><span class="pre">instance_class</span></code> sizes.</p>
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
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html">docs</a> about the details.</li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``aws_docdb_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html</a>&gt;`_ in which to launch this instance.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the DocDB instance. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code>.</li>
<li><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifer</span></code>.</li>
<li><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use. For details on CPU and memory, see [Scaling for DocDB Instances][2]. DocDB currently
supports the below instance classes. Please see [AWS Documentation][4] for complete details.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</li>
<li><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html">docs</a> about the details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``aws_docdb_cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html</a>&gt;`_ in which to launch this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.db_subnet_group_name">
<code class="descname">db_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB subnet group to associate with this DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.dbi_resource_id">
<code class="descname">dbi_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.dbi_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region-unique, immutable identifier for the DB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address for this instance. May not be writable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for the DocDB instance. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.identifier_prefix">
<code class="descname">identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifer</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.instance_class">
<code class="descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance class to use. For details on CPU and memory, see [Scaling for DocDB Instances][2]. DocDB currently
supports the below instance classes. Please see [AWS Documentation][4] for complete details.</p>
<ul class="simple">
<li>db.r4.large</li>
<li>db.r4.xlarge</li>
<li>db.r4.2xlarge</li>
<li>db.r4.4xlarge</li>
<li>db.r4.8xlarge</li>
<li>db.r4.16xlarge</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key if one is set to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The database port</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.promotion_tier">
<code class="descname">promotion_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.promotion_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.writer">
<code class="descname">writer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.writer" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.ClusterInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocumentDB Cluster Parameter Group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the documentDB cluster parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the documentDB parameter.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of documentDB parameters to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_parameter_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_parameter_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the documentDB parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of documentDB parameters to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterSnapshot">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">ClusterSnapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>db_cluster_identifier=None</em>, <em>db_cluster_snapshot_identifier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocDB database cluster snapshot for DocDB clusters.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DocDB Cluster Identifier from which to take the snapshot.</li>
<li><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_cluster_snapshot.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_identifier">
<code class="descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DocDB Cluster Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_arn">
<code class="descname">db_cluster_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_identifier">
<code class="descname">db_cluster_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DocDB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DocDB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DocDB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DocDB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DocDB cluster snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.ClusterSnapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterSnapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an DocumentDB subnet group resource.</p>
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
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_subnet_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/docdb_subnet_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the docDB subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
