<div class="section" id="module-pulumi_aws.neptune">
<span id="neptune"></span><h1>neptune<a class="headerlink" href="#module-pulumi_aws.neptune" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.neptune.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>apply_immediately=None</em>, <em>availability_zones=None</em>, <em>backup_retention_period=None</em>, <em>cluster_identifier=None</em>, <em>cluster_identifier_prefix=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>final_snapshot_identifier=None</em>, <em>iam_database_authentication_enabled=None</em>, <em>iam_roles=None</em>, <em>kms_key_arn=None</em>, <em>neptune_cluster_parameter_group_name=None</em>, <em>neptune_subnet_group_name=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>replication_source_identifier=None</em>, <em>skip_final_snapshot=None</em>, <em>snapshot_identifier=None</em>, <em>storage_encrypted=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Neptune Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of Neptune Cluster Instances.</p>
<p>Changes to a Neptune Cluster can occur when you manually change a
parameter, such as <cite>backup_retention_period</cite>, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
<cite>apply_immediately</cite> flag to instruct the service to apply the change immediately
(see documentation below).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is <cite>false</cite>.</li>
<li><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.</li>
<li><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The days to retain backups for. Default <cite>1</cite></li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier. If omitted, Terraform will assign a random, unique identifier.</li>
<li><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <cite>cluster_identifer</cite>.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this Neptune cluster. Defaults to <cite>neptune</cite>.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version.</li>
<li><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.</li>
<li><strong>iam_database_authentication_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.</li>
<li><strong>iam_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of ARNs for the IAM roles to associate to the Neptune Cluster.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <cite>kms_key_arn</cite>, <cite>storage_encrypted</cite> needs to be set to true.</li>
<li><strong>neptune_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</li>
<li><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Neptune subnet group to associate with this Neptune instance.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port on which the Neptune accepts connections. Default is <cite>8182</cite>.</li>
<li><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</li>
<li><strong>replication_source_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.</li>
<li><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from <cite>final_snapshot_identifier</cite>. Default is <cite>false</cite>.</li>
<li><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.</li>
<li><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the Neptune cluster is encrypted. The default is <cite>false</cite> if not specified.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Neptune cluster.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate with the Cluster</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune Cluster Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.backup_retention_period">
<code class="descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Default <cite>1</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster identifier. If omitted, Terraform will assign a random, unique identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_identifier_prefix">
<code class="descname">cluster_identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <cite>cluster_identifer</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_members">
<code class="descname">cluster_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Neptune Instances that are a part of this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_resource_id">
<code class="descname">cluster_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune Cluster Resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address of the Neptune instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for this Neptune cluster. Defaults to <cite>neptune</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.final_snapshot_identifier">
<code class="descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route53 Hosted Zone ID of the endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.iam_database_authentication_enabled">
<code class="descname">iam_database_authentication_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.iam_database_authentication_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.iam_roles">
<code class="descname">iam_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of ARNs for the IAM roles to associate to the Neptune Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <cite>kms_key_arn</cite>, <cite>storage_encrypted</cite> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.neptune_cluster_parameter_group_name">
<code class="descname">neptune_cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.neptune_cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A cluster parameter group to associate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.neptune_subnet_group_name">
<code class="descname">neptune_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.neptune_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A Neptune subnet group to associate with this Neptune instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the Neptune accepts connections. Default is <cite>8182</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.reader_endpoint">
<code class="descname">reader_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.reader_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.replication_source_identifier">
<code class="descname">replication_source_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.replication_source_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.skip_final_snapshot">
<code class="descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from <cite>final_snapshot_identifier</cite>. Default is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.snapshot_identifier">
<code class="descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the Neptune cluster is encrypted. The default is <cite>false</cite> if not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Neptune cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to associate with the Cluster</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">ClusterInstance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>cluster_identifier=None</em>, <em>engine=None</em>, <em>engine_version=None</em>, <em>identifier=None</em>, <em>identifier_prefix=None</em>, <em>instance_class=None</em>, <em>neptune_parameter_group_name=None</em>, <em>neptune_subnet_group_name=None</em>, <em>port=None</em>, <em>preferred_backup_window=None</em>, <em>preferred_maintenance_window=None</em>, <em>promotion_tier=None</em>, <em>publicly_accessible=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.</p>
<p>You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various <cite>instance_class</cite> sizes.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.</li>
<li><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is <cite>true</cite>.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the neptune instance is created in.</li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the [<cite>aws_neptune_cluster</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>) in which to launch this instance.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the neptune instance. Defaults to <cite>neptune</cite>. Valid Values: <cite>neptune</cite>.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The neptune engine version.</li>
<li><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.</li>
<li><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <cite>identifer</cite>.</li>
<li><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use.</li>
<li><strong>neptune_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter group to associate with this instance.</li>
<li><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with this neptune instance. <strong>NOTE:</strong> This must match the <cite>neptune_subnet_group_name</cite> of the attached [<cite>aws_neptune_cluster</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>).</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port on which the DB accepts connections. Defaults to <cite>8182</cite>.</li>
<li><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled. Eg: “04:00-09:00”</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</li>
<li><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool to control if instance is publicly accessible. Default is <cite>false</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the instance. See also <cite>endpoint</cite> and <cite>port</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of neptune instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the neptune instance is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the [<cite>aws_neptune_cluster</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>) in which to launch this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.dbi_resource_id">
<code class="descname">dbi_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.dbi_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region-unique, immutable identifier for the neptune instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection endpoint in <cite>address:port</cite> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for the neptune instance. Defaults to <cite>neptune</cite>. Valid Values: <cite>neptune</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The neptune engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.identifier">
<code class="descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.identifier_prefix">
<code class="descname">identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique identifier beginning with the specified prefix. Conflicts with <cite>identifer</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.instance_class">
<code class="descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance class to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key if one is set to the neptune cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.neptune_parameter_group_name">
<code class="descname">neptune_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.neptune_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune parameter group to associate with this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.neptune_subnet_group_name">
<code class="descname">neptune_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.neptune_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet group to associate with this neptune instance. <strong>NOTE:</strong> This must match the <cite>neptune_subnet_group_name</cite> of the attached [<cite>aws_neptune_cluster</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections. Defaults to <cite>8182</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.preferred_backup_window">
<code class="descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled. Eg: “04:00-09:00”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.promotion_tier">
<code class="descname">promotion_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.promotion_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Bool to control if instance is publicly accessible. Default is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the neptune cluster is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.writer">
<code class="descname">writer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.writer" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating if this instance is writable. <cite>False</cite> indicates this instance is a read replica.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>parameters=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune Cluster Parameter Group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune cluster parameter group. Defaults to “Managed by Terraform”.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the neptune cluster parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of neptune parameters to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the neptune cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the neptune cluster parameter group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the neptune cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of neptune parameters to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterSnapshot">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">ClusterSnapshot</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>db_cluster_identifier=None</em>, <em>db_cluster_snapshot_identifier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune database cluster snapshot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB Cluster Identifier from which to take the snapshot.</li>
<li><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_identifier">
<code class="descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB Cluster Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_arn">
<code class="descname">db_cluster_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_identifier">
<code class="descname">db_cluster_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.license_model">
<code class="descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.storage_encrypted">
<code class="descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DB cluster snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterSnapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterSnapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.EventSubscription">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">EventSubscription</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>enabled=None</em>, <em>event_categories=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>sns_topic_arn=None</em>, <em>source_ids=None</em>, <em>source_type=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EventSubscription resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable the subscription. Defaults to true.</li>
<li><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event categories for a <cite>source_type</cite> that you want to subscribe to. Run <cite>aws neptune describe-event-categories</cite> to find all the event categories.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. By default generated by Terraform.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. Conflicts with <cite>name</cite>.</li>
<li><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic to send events to.</li>
<li><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a <cite>source_type</cite> must also be specified.</li>
<li><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source that will be generating the events. Valid options are <cite>db-instance</cite>, <cite>db-security-group</cite>, <cite>db-parameter-group</cite>, <cite>db-snapshot</cite>, <cite>db-cluster</cite> or <cite>db-cluster-snapshot</cite>. If not set, all sources will be subscribed to.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable the subscription. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.event_categories">
<code class="descname">event_categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of event categories for a <cite>source_type</cite> that you want to subscribe to. Run <cite>aws neptune describe-event-categories</cite> to find all the event categories.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune event subscription. By default generated by Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune event subscription. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.sns_topic_arn">
<code class="descname">sns_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic to send events to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.source_ids">
<code class="descname">source_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.source_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a <cite>source_type</cite> must also be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.source_type">
<code class="descname">source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source that will be generating the events. Valid options are <cite>db-instance</cite>, <cite>db-security-group</cite>, <cite>db-parameter-group</cite>, <cite>db-snapshot</cite>, <cite>db-cluster</cite> or <cite>db-cluster-snapshot</cite>. If not set, all sources will be subscribed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.EventSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.EventSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">ParameterGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune Parameter Group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Neptune parameter group. Defaults to “Managed by Terraform”.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the Neptune parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune parameter.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Neptune parameters to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune parameter group Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Neptune parameter group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the Neptune parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Neptune parameters to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.neptune.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Neptune subnet group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune subnet group. Defaults to “Managed by Terraform”.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the neptune subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the neptune subnet group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
