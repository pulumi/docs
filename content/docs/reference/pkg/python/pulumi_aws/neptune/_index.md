---
title: Module neptune
title_tag: Module neptune | Package pulumi_aws | Python SDK
linktitle: neptune
notitle: true
---

<div class="section" id="neptune">
<h1>neptune<a class="headerlink" href="#neptune" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.neptune"></span><dl class="class">
<dt id="pulumi_aws.neptune.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">backup_retention_period=None</em>, <em class="sig-param">cluster_identifier=None</em>, <em class="sig-param">cluster_identifier_prefix=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">enable_cloudwatch_logs_exports=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">final_snapshot_identifier=None</em>, <em class="sig-param">iam_database_authentication_enabled=None</em>, <em class="sig-param">iam_roles=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">neptune_cluster_parameter_group_name=None</em>, <em class="sig-param">neptune_subnet_group_name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">preferred_backup_window=None</em>, <em class="sig-param">preferred_maintenance_window=None</em>, <em class="sig-param">replication_source_identifier=None</em>, <em class="sig-param">skip_final_snapshot=None</em>, <em class="sig-param">snapshot_identifier=None</em>, <em class="sig-param">storage_encrypted=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_security_group_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Neptune Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of Neptune Cluster Instances.</p>
<p>Changes to a Neptune Cluster can occur when you manually change a
parameter, such as <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code>, and are reflected in the next maintenance
window. Because of this, this provider may report a difference in its planning
phase because a modification has not yet taken place. You can use the
<code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> flag to instruct the service to apply the change immediately
(see documentation below).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code>.</p></li>
<li><p><strong>enable_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the log types this DB cluster is configured to export to Cloudwatch Logs. Currently only supports <code class="docutils literal notranslate"><span class="pre">audit</span></code>.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this Neptune cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version.</p></li>
<li><p><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.</p></li>
<li><p><strong>iam_database_authentication_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.</p></li>
<li><p><strong>iam_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of ARNs for the IAM roles to associate to the Neptune Cluster.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>neptune_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</p></li>
<li><p><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Neptune subnet group to associate with this Neptune instance.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the Neptune accepts connections. Default is <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</p></li>
<li><p><strong>replication_source_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.</p></li>
<li><p><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the Neptune cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> if not specified.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Neptune cluster.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate with the Cluster</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune Cluster Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.backup_retention_period">
<code class="sig-name descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_identifier">
<code class="sig-name descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_identifier_prefix">
<code class="sig-name descname">cluster_identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_members">
<code class="sig-name descname">cluster_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Neptune Instances that are a part of this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.cluster_resource_id">
<code class="sig-name descname">cluster_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune Cluster Resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.enable_cloudwatch_logs_exports">
<code class="sig-name descname">enable_cloudwatch_logs_exports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.enable_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the log types this DB cluster is configured to export to Cloudwatch Logs. Currently only supports <code class="docutils literal notranslate"><span class="pre">audit</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address of the Neptune instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for this Neptune cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.final_snapshot_identifier">
<code class="sig-name descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route53 Hosted Zone ID of the endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.iam_database_authentication_enabled">
<code class="sig-name descname">iam_database_authentication_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.iam_database_authentication_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.iam_roles">
<code class="sig-name descname">iam_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of ARNs for the IAM roles to associate to the Neptune Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.neptune_cluster_parameter_group_name">
<code class="sig-name descname">neptune_cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.neptune_cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A cluster parameter group to associate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.neptune_subnet_group_name">
<code class="sig-name descname">neptune_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.neptune_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A Neptune subnet group to associate with this Neptune instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the Neptune accepts connections. Default is <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.preferred_backup_window">
<code class="sig-name descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.preferred_maintenance_window">
<code class="sig-name descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.reader_endpoint">
<code class="sig-name descname">reader_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.reader_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.replication_source_identifier">
<code class="sig-name descname">replication_source_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.replication_source_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.skip_final_snapshot">
<code class="sig-name descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.snapshot_identifier">
<code class="sig-name descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the Neptune cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> if not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Neptune cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.Cluster.vpc_security_group_ids">
<code class="sig-name descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to associate with the Cluster</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">backup_retention_period=None</em>, <em class="sig-param">cluster_identifier=None</em>, <em class="sig-param">cluster_identifier_prefix=None</em>, <em class="sig-param">cluster_members=None</em>, <em class="sig-param">cluster_resource_id=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">enable_cloudwatch_logs_exports=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">final_snapshot_identifier=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">iam_database_authentication_enabled=None</em>, <em class="sig-param">iam_roles=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">neptune_cluster_parameter_group_name=None</em>, <em class="sig-param">neptune_subnet_group_name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">preferred_backup_window=None</em>, <em class="sig-param">preferred_maintenance_window=None</em>, <em class="sig-param">reader_endpoint=None</em>, <em class="sig-param">replication_source_identifier=None</em>, <em class="sig-param">skip_final_snapshot=None</em>, <em class="sig-param">snapshot_identifier=None</em>, <em class="sig-param">storage_encrypted=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_security_group_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neptune Cluster Amazon Resource Name (ARN)</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code>.</p></li>
<li><p><strong>cluster_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Neptune Instances that are a part of this cluster</p></li>
<li><p><strong>cluster_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neptune Cluster Resource ID</p></li>
<li><p><strong>enable_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the log types this DB cluster is configured to export to Cloudwatch Logs. Currently only supports <code class="docutils literal notranslate"><span class="pre">audit</span></code>.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS address of the Neptune instance</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this Neptune cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version.</p></li>
<li><p><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.</p></li>
<li><p><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Route53 Hosted Zone ID of the endpoint</p></li>
<li><p><strong>iam_database_authentication_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.</p></li>
<li><p><strong>iam_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of ARNs for the IAM roles to associate to the Neptune Cluster.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>neptune_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</p></li>
<li><p><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Neptune subnet group to associate with this Neptune instance.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the Neptune accepts connections. Default is <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30</p></li>
<li><p><strong>reader_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas</p></li>
<li><p><strong>replication_source_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.</p></li>
<li><p><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the Neptune cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> if not specified.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Neptune cluster.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate with the Cluster</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">ClusterInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">cluster_identifier=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">identifier_prefix=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">neptune_parameter_group_name=None</em>, <em class="sig-param">neptune_subnet_group_name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">preferred_backup_window=None</em>, <em class="sig-param">preferred_maintenance_window=None</em>, <em class="sig-param">promotion_tier=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.</p>
<p>You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various <code class="docutils literal notranslate"><span class="pre">instance_class</span></code> sizes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the neptune instance is created in.</p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_ in which to launch this instance.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the neptune instance. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The neptune engine version.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use.</p></li>
<li><p><strong>neptune_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter group to associate with this instance.</p></li>
<li><p><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with this neptune instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">neptune_subnet_group_name</span></code> of the attached <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections. Defaults to <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled. Eg: “04:00-09:00”</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p></li>
<li><p><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool to control if instance is publicly accessible. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the instance. See also <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> and <code class="docutils literal notranslate"><span class="pre">port</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of neptune instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.auto_minor_version_upgrade">
<code class="sig-name descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the neptune instance is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.cluster_identifier">
<code class="sig-name descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_ in which to launch this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.dbi_resource_id">
<code class="sig-name descname">dbi_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.dbi_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region-unique, immutable identifier for the neptune instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection endpoint in <code class="docutils literal notranslate"><span class="pre">address:port</span></code> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for the neptune instance. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The neptune engine version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.identifier">
<code class="sig-name descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.identifier_prefix">
<code class="sig-name descname">identifier_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.instance_class">
<code class="sig-name descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance class to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key if one is set to the neptune cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.neptune_parameter_group_name">
<code class="sig-name descname">neptune_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.neptune_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune parameter group to associate with this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.neptune_subnet_group_name">
<code class="sig-name descname">neptune_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.neptune_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet group to associate with this neptune instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">neptune_subnet_group_name</span></code> of the attached <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections. Defaults to <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.preferred_backup_window">
<code class="sig-name descname">preferred_backup_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled. Eg: “04:00-09:00”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.preferred_maintenance_window">
<code class="sig-name descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.promotion_tier">
<code class="sig-name descname">promotion_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.promotion_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.publicly_accessible">
<code class="sig-name descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Bool to control if instance is publicly accessible. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the neptune cluster is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterInstance.writer">
<code class="sig-name descname">writer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.writer" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">cluster_identifier=None</em>, <em class="sig-param">dbi_resource_id=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">identifier_prefix=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">neptune_parameter_group_name=None</em>, <em class="sig-param">neptune_subnet_group_name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">preferred_backup_window=None</em>, <em class="sig-param">preferred_maintenance_window=None</em>, <em class="sig-param">promotion_tier=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">storage_encrypted=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">writer=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname of the instance. See also <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> and <code class="docutils literal notranslate"><span class="pre">port</span></code>.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of neptune instance</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the neptune instance is created in.</p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_ in which to launch this instance.</p></li>
<li><p><strong>dbi_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region-unique, immutable identifier for the neptune instance.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection endpoint in <code class="docutils literal notranslate"><span class="pre">address:port</span></code> format.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the neptune instance. Defaults to <code class="docutils literal notranslate"><span class="pre">neptune</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">neptune</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The neptune engine version.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifier</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key if one is set to the neptune cluster.</p></li>
<li><p><strong>neptune_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter group to associate with this instance.</p></li>
<li><p><strong>neptune_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with this neptune instance. <strong>NOTE:</strong> This must match the <code class="docutils literal notranslate"><span class="pre">neptune_subnet_group_name</span></code> of the attached <cite>``neptune.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html">https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html</a>&gt;`_.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections. Defaults to <code class="docutils literal notranslate"><span class="pre">8182</span></code>.</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled. Eg: “04:00-09:00”</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p></li>
<li><p><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool to control if instance is publicly accessible. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the neptune cluster is encrypted.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</p></li>
<li><p><strong>writer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterParameterGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune Cluster Parameter Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune cluster parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the neptune cluster parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of neptune parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the neptune parameter.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the neptune cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the neptune cluster parameter group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.family">
<code class="sig-name descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the neptune cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of neptune parameters to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the neptune parameter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterParameterGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the neptune cluster parameter group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune cluster parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the neptune cluster parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune parameter.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of neptune parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the neptune parameter.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterParameterGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ClusterSnapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">ClusterSnapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_cluster_identifier=None</em>, <em class="sig-param">db_cluster_snapshot_identifier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune database cluster snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB Cluster Identifier from which to take the snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.allocated_storage">
<code class="sig-name descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the allocated storage size in gigabytes (GB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_identifier">
<code class="sig-name descname">db_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB Cluster Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_arn">
<code class="sig-name descname">db_cluster_snapshot_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_identifier">
<code class="sig-name descname">db_cluster_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.db_cluster_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.license_model">
<code class="sig-name descname">license_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.license_model" title="Permalink to this definition">¶</a></dt>
<dd><p>License model information for the restored DB cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DB Cluster Snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ClusterSnapshot.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DB cluster snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterSnapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_storage=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">db_cluster_identifier=None</em>, <em class="sig-param">db_cluster_snapshot_arn=None</em>, <em class="sig-param">db_cluster_snapshot_identifier=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">license_model=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">snapshot_type=None</em>, <em class="sig-param">source_db_cluster_snapshot_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">storage_encrypted=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterSnapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the allocated storage size in gigabytes (GB).</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.</p></li>
<li><p><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB Cluster Identifier from which to take the snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the DB Cluster Snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the database engine.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the database engine for this DB cluster snapshot.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.</p></li>
<li><p><strong>license_model</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – License model information for the restored DB cluster.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port that the DB cluster was listening on at the time of the snapshot.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of this DB Cluster Snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster snapshot is encrypted.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID associated with the DB cluster snapshot.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterSnapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ClusterSnapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ClusterSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.EventSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">EventSubscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_categories=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">sns_topic_arn=None</em>, <em class="sig-param">source_ids=None</em>, <em class="sig-param">source_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>The following additional atttributes are provided:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The name of the Neptune event notification subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> - The Amazon Resource Name of the Neptune event notification subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customer_aws_id</span></code> - The AWS customer account associated with the Neptune event notification subscription.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable the subscription. Defaults to true.</p></li>
<li><p><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event categories for a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> that you want to subscribe to. Run <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">neptune</span> <span class="pre">describe-event-categories</span></code> to find all the event categories.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic to send events to.</p></li>
<li><p><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> must also be specified.</p></li>
<li><p><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source that will be generating the events. Valid options are <code class="docutils literal notranslate"><span class="pre">db-instance</span></code>, <code class="docutils literal notranslate"><span class="pre">db-security-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-parameter-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-snapshot</span></code>, <code class="docutils literal notranslate"><span class="pre">db-cluster</span></code> or <code class="docutils literal notranslate"><span class="pre">db-cluster-snapshot</span></code>. If not set, all sources will be subscribed to.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable the subscription. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.event_categories">
<code class="sig-name descname">event_categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of event categories for a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> that you want to subscribe to. Run <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">neptune</span> <span class="pre">describe-event-categories</span></code> to find all the event categories.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune event subscription. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune event subscription. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.sns_topic_arn">
<code class="sig-name descname">sns_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic to send events to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.source_ids">
<code class="sig-name descname">source_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.source_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> must also be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.source_type">
<code class="sig-name descname">source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source that will be generating the events. Valid options are <code class="docutils literal notranslate"><span class="pre">db-instance</span></code>, <code class="docutils literal notranslate"><span class="pre">db-security-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-parameter-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-snapshot</span></code>, <code class="docutils literal notranslate"><span class="pre">db-cluster</span></code> or <code class="docutils literal notranslate"><span class="pre">db-cluster-snapshot</span></code>. If not set, all sources will be subscribed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.EventSubscription.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.EventSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">customer_aws_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_categories=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">sns_topic_arn=None</em>, <em class="sig-param">source_ids=None</em>, <em class="sig-param">source_type=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable the subscription. Defaults to true.</p></li>
<li><p><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event categories for a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> that you want to subscribe to. Run <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">neptune</span> <span class="pre">describe-event-categories</span></code> to find all the event categories.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune event subscription. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic to send events to.</p></li>
<li><p><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a <code class="docutils literal notranslate"><span class="pre">source_type</span></code> must also be specified.</p></li>
<li><p><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source that will be generating the events. Valid options are <code class="docutils literal notranslate"><span class="pre">db-instance</span></code>, <code class="docutils literal notranslate"><span class="pre">db-security-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-parameter-group</span></code>, <code class="docutils literal notranslate"><span class="pre">db-snapshot</span></code>, <code class="docutils literal notranslate"><span class="pre">db-cluster</span></code> or <code class="docutils literal notranslate"><span class="pre">db-cluster-snapshot</span></code>. If not set, all sources will be subscribed to.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.EventSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.EventSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.ParameterGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">ParameterGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Neptune Parameter Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Neptune parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the Neptune parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune parameter.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Neptune parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The apply method of the Neptune parameter. Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the Neptune parameter.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neptune parameter group Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Neptune parameter group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.family">
<code class="sig-name descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the Neptune parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Neptune parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Neptune parameters to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The apply method of the Neptune parameter. Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the Neptune parameter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.ParameterGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ParameterGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ParameterGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neptune parameter group Amazon Resource Name (ARN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Neptune parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the Neptune parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Neptune parameter.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Neptune parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The apply method of the Neptune parameter. Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Neptune parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the Neptune parameter.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ParameterGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.ParameterGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.neptune.SubnetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.neptune.</code><code class="sig-name descname">SubnetGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Neptune subnet group resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune subnet group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the neptune subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the neptune subnet group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the neptune subnet group. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.neptune.SubnetGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.SubnetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the neptune subnet group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the neptune subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the neptune subnet group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.SubnetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.neptune.SubnetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.neptune.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
