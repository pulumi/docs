---
title: Module docdb
title_tag: Module docdb | Package pulumi_aws | Python SDK
linktitle: docdb
notitle: true
---

<div class="section" id="docdb">
<h1>docdb<a class="headerlink" href="#docdb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.docdb"></span><dl class="py class">
<dt id="pulumi_aws.docdb.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.docdb.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cloudwatch_logs_exports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">final_snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_final_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocDB Cluster.</p>
<p>Changes to a DocDB Cluster can occur when you manually change a
parameter, such as <code class="docutils literal notranslate"><span class="pre">port</span></code>, and are reflected in the next maintenance
window. Because of this, this provider may report a difference in its planning
phase because a modification has not yet taken place. You can use the
<code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> flag to instruct the service to apply the change immediately
(see documentation below).</p>
<blockquote>
<div><p><strong>Note:</strong> using <code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> can result in a brief downtime as the server reboots.
<strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">docdb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;docdb&quot;</span><span class="p">,</span>
    <span class="n">backup_retention_period</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">cluster_identifier</span><span class="o">=</span><span class="s2">&quot;my-docdb-cluster&quot;</span><span class="p">,</span>
    <span class="n">engine</span><span class="o">=</span><span class="s2">&quot;docdb&quot;</span><span class="p">,</span>
    <span class="n">master_password</span><span class="o">=</span><span class="s2">&quot;mustbeeightchars&quot;</span><span class="p">,</span>
    <span class="n">master_username</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">preferred_backup_window</span><span class="o">=</span><span class="s2">&quot;07:00-09:00&quot;</span><span class="p">,</span>
    <span class="n">skip_final_snapshot</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that
instances in the DB cluster can be created in.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifer</span></code>.</p></li>
<li><p><strong>cluster_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DocDB Instances that are a part of this cluster</p></li>
<li><p><strong>db_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</p></li>
<li><p><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A DB subnet group to associate with this DB instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A value that indicates whether the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.</p></li>
<li><p><strong>enabled_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">profiler</span></code>.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version. Updating this argument results in an outage.</p></li>
<li><p><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>master_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.</p></li>
<li><p><strong>master_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for the master DB user.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p></li>
<li><p><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the DB cluster.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate
with the Cluster</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EC2 Availability Zones that
instances in the DB cluster can be created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.backup_retention_period">
<code class="sig-name descname">backup_retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_identifier">
<code class="sig-name descname">cluster_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_identifier_prefix">
<code class="sig-name descname">cluster_identifier_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifer</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_members">
<code class="sig-name descname">cluster_members</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DocDB Instances that are a part of this cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.cluster_resource_id">
<code class="sig-name descname">cluster_resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.cluster_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DocDB Cluster Resource ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.db_cluster_parameter_group_name">
<code class="sig-name descname">db_cluster_parameter_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.db_cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A cluster parameter group to associate with the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.db_subnet_group_name">
<code class="sig-name descname">db_subnet_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A DB subnet group to associate with this DB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>A value that indicates whether the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.enabled_cloudwatch_logs_exports">
<code class="sig-name descname">enabled_cloudwatch_logs_exports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.enabled_cloudwatch_logs_exports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">profiler</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address of the DocDB instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version. Updating this argument results in an outage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.final_snapshot_identifier">
<code class="sig-name descname">final_snapshot_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route53 Hosted Zone ID of the endpoint</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.master_password">
<code class="sig-name descname">master_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.master_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.master_username">
<code class="sig-name descname">master_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the master DB user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the DB accepts connections</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.preferred_backup_window">
<code class="sig-name descname">preferred_backup_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.reader_endpoint">
<code class="sig-name descname">reader_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.reader_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.skip_final_snapshot">
<code class="sig-name descname">skip_final_snapshot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.snapshot_identifier">
<code class="sig-name descname">snapshot_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the DB cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.Cluster.vpc_security_group_ids">
<code class="sig-name descname">vpc_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security groups to associate
with the Cluster</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cloudwatch_logs_exports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">final_snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosted_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reader_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_final_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of cluster</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 Availability Zones that
instances in the DB cluster can be created in.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The days to retain backups for. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster identifier. If omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>cluster_identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique cluster identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">cluster_identifer</span></code>.</p></li>
<li><p><strong>cluster_members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DocDB Instances that are a part of this cluster</p></li>
<li><p><strong>cluster_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DocDB Cluster Resource ID</p></li>
<li><p><strong>db_cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cluster parameter group to associate with the cluster.</p></li>
<li><p><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A DB subnet group to associate with this DB instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A value that indicates whether the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.</p></li>
<li><p><strong>enabled_cloudwatch_logs_exports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: <code class="docutils literal notranslate"><span class="pre">audit</span></code>, <code class="docutils literal notranslate"><span class="pre">profiler</span></code>.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS address of the DocDB instance</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for this DB cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version. Updating this argument results in an outage.</p></li>
<li><p><strong>final_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.</p></li>
<li><p><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Route53 Hosted Zone ID of the endpoint</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">storage_encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>master_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.</p></li>
<li><p><strong>master_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for the master DB user.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the DB accepts connections</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00</p></li>
<li><p><strong>reader_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas</p></li>
<li><p><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from <code class="docutils literal notranslate"><span class="pre">final_snapshot_identifier</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the DB cluster.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC security groups to associate
with the Cluster</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.docdb.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.docdb.ClusterInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.docdb.</code><code class="sig-name descname">ClusterInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">promotion_tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an DocDB Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">DocDB Cluster</a>.</p>
<p>You do not designate a primary and subsequent replicas. Instead, you simply add DocDB
Instances and DocDB manages the replication. You can use the <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#count">count</a>
meta-parameter to make multiple instances and join them all to the same DocDB
Cluster, or you may specify different Cluster Instance resources with various
<code class="docutils literal notranslate"><span class="pre">instance_class</span></code> sizes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">availability_zones</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;us-west-2a&quot;</span><span class="p">,</span>
        <span class="s2">&quot;us-west-2b&quot;</span><span class="p">,</span>
        <span class="s2">&quot;us-west-2c&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">cluster_identifier</span><span class="o">=</span><span class="s2">&quot;docdb-cluster-demo&quot;</span><span class="p">,</span>
    <span class="n">master_password</span><span class="o">=</span><span class="s2">&quot;barbut8chars&quot;</span><span class="p">,</span>
    <span class="n">master_username</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">cluster_instances</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]:</span>
    <span class="n">cluster_instances</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">ClusterInstance</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;clusterInstances-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">cluster_identifier</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">identifier</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;docdb-cluster-demo-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">instance_class</span><span class="o">=</span><span class="s2">&quot;db.r5.large&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html">docs</a> about the details.</p></li>
<li><p><strong>ca_cert_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional) The identifier of the CA certificate for the DB instance.</p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``docdb.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html</a>&gt;`_ in which to launch this instance.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the DocDB instance. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code>.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The indentifier for the DocDB instance, if omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifer</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance class to use. For details on CPU and memory, see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-manage-performance.html#db-cluster-manage-scaling-instance">Scaling for DocDB Instances</a>. DocDB currently
supports the below instance classes. Please see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-classes.html#db-instance-class-specs">AWS Documentation</a> for complete details.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="n">large</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">2</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">4</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">8</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">16</span><span class="n">xlarge</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p></li>
<li><p><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of cluster instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.auto_minor_version_upgrade">
<code class="sig-name descname">auto_minor_version_upgrade</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html">docs</a> about the details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.ca_cert_identifier">
<code class="sig-name descname">ca_cert_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.ca_cert_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The identifier of the CA certificate for the DB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.cluster_identifier">
<code class="sig-name descname">cluster_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``docdb.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html</a>&gt;`_ in which to launch this instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.db_subnet_group_name">
<code class="sig-name descname">db_subnet_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.db_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DB subnet group to associate with this DB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.dbi_resource_id">
<code class="sig-name descname">dbi_resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.dbi_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region-unique, immutable identifier for the DB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address for this instance. May not be writable</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database engine to be used for the DocDB instance. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The database engine version</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.identifier">
<code class="sig-name descname">identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The indentifier for the DocDB instance, if omitted, this provider will assign a random, unique identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.identifier_prefix">
<code class="sig-name descname">identifier_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.identifier_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifer</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.instance_class">
<code class="sig-name descname">instance_class</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance class to use. For details on CPU and memory, see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-manage-performance.html#db-cluster-manage-scaling-instance">Scaling for DocDB Instances</a>. DocDB currently
supports the below instance classes. Please see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-classes.html#db-instance-class-specs">AWS Documentation</a> for complete details.</p>
<ul class="simple">
<li><p>db.r4.large</p></li>
<li><p>db.r4.xlarge</p></li>
<li><p>db.r4.2xlarge</p></li>
<li><p>db.r4.4xlarge</p></li>
<li><p>db.r4.8xlarge</p></li>
<li><p>db.r4.16xlarge</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key if one is set to the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The database port</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.preferred_backup_window">
<code class="sig-name descname">preferred_backup_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.preferred_backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range during which automated backups are created if automated backups are enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.preferred_maintenance_window">
<code class="sig-name descname">preferred_maintenance_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.promotion_tier">
<code class="sig-name descname">promotion_tier</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.promotion_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DB cluster is encrypted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterInstance.writer">
<code class="sig-name descname">writer</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.writer" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dbi_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">promotion_tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publicly_accessible</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">writer</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of cluster instance</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The EC2 Availability Zone that the DB instance is created in. See <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html">docs</a> about the details.</p>
</p></li>
<li><p><strong>ca_cert_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional) The identifier of the CA certificate for the DB instance.</p></li>
<li><p><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``docdb.Cluster`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html">https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html</a>&gt;`_ in which to launch this instance.</p></li>
<li><p><strong>db_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DB subnet group to associate with this DB instance.</p></li>
<li><p><strong>dbi_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region-unique, immutable identifier for the DB instance.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS address for this instance. May not be writable</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database engine to be used for the DocDB instance. Defaults to <code class="docutils literal notranslate"><span class="pre">docdb</span></code>. Valid Values: <code class="docutils literal notranslate"><span class="pre">docdb</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database engine version</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The indentifier for the DocDB instance, if omitted, this provider will assign a random, unique identifier.</p></li>
<li><p><strong>identifier_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique identifier beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">identifer</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The instance class to use. For details on CPU and memory, see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-manage-performance.html#db-cluster-manage-scaling-instance">Scaling for DocDB Instances</a>. DocDB currently
supports the below instance classes. Please see <a class="reference external" href="https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-classes.html#db-instance-class-specs">AWS Documentation</a> for complete details.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="n">large</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">2</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">4</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">8</span><span class="n">xlarge</span>
<span class="o">-</span> <span class="n">db</span><span class="o">.</span><span class="n">r4</span><span class="o">.</span><span class="mi">16</span><span class="n">xlarge</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key if one is set to the cluster.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The database port</p></li>
<li><p><strong>preferred_backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range during which automated backups are created if automated backups are enabled.</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The window to perform maintenance in.
Syntax: “ddd:hh24:mi-ddd:hh24:mi”. Eg: “Mon:00:00-Mon:03:00”.</p></li>
<li><p><strong>promotion_tier</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DB cluster is encrypted.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the instance.</p></li>
<li><p><strong>writer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating if this instance is writable. <code class="docutils literal notranslate"><span class="pre">False</span></code> indicates this instance is a read replica.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.docdb.ClusterParameterGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.docdb.</code><code class="sig-name descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocumentDB Cluster Parameter Group</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">ClusterParameterGroup</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;docdb cluster parameter group&quot;</span><span class="p">,</span>
    <span class="n">family</span><span class="o">=</span><span class="s2">&quot;docdb3.6&quot;</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;tls&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;enabled&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the documentDB cluster parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the documentDB cluster parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the documentDB parameter.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of documentDB parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the documentDB parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the documentDB parameter.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the documentDB cluster parameter group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.family">
<code class="sig-name descname">family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the documentDB parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of documentDB parameters to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the documentDB parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the documentDB parameter.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterParameterGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the documentDB cluster parameter group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the documentDB cluster parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the documentDB cluster parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the documentDB parameter.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of documentDB parameters to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">immediate</span></code> and <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending-reboot</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the documentDB parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the documentDB parameter.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.docdb.ClusterSnapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.docdb.</code><code class="sig-name descname">ClusterSnapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocDB database cluster snapshot for DocDB clusters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">ClusterSnapshot</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">db_cluster_identifier</span><span class="o">=</span><span class="n">aws_docdb_cluster</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">db_cluster_snapshot_identifier</span><span class="o">=</span><span class="s2">&quot;resourcetestsnapshot1234&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DocDB Cluster Identifier from which to take the snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_identifier">
<code class="sig-name descname">db_cluster_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The DocDB Cluster Identifier from which to take the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_arn">
<code class="sig-name descname">db_cluster_snapshot_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_identifier">
<code class="sig-name descname">db_cluster_snapshot_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.db_cluster_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the database engine.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the database engine for this DocDB cluster snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port that the DocDB cluster was listening on at the time of the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this DocDB Cluster Snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.storage_encrypted">
<code class="sig-name descname">storage_encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.storage_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the DocDB cluster snapshot is encrypted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.ClusterSnapshot.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID associated with the DocDB cluster snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterSnapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_snapshot_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_cluster_snapshot_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_db_cluster_snapshot_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterSnapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.</p></li>
<li><p><strong>db_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DocDB Cluster Identifier from which to take the snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.</p></li>
<li><p><strong>db_cluster_snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for the snapshot.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the database engine.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the database engine for this DocDB cluster snapshot.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port that the DocDB cluster was listening on at the time of the snapshot.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of this DocDB Cluster Snapshot.</p></li>
<li><p><strong>storage_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the DocDB cluster snapshot is encrypted.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID associated with the DocDB cluster snapshot.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterSnapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.docdb.ClusterSnapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.docdb.SubnetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.docdb.</code><code class="sig-name descname">SubnetGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an DocumentDB subnet group resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">docdb</span><span class="o">.</span><span class="n">SubnetGroup</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;frontend&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;backend&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;My docdb subnet group&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the docDB subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the docDB subnet group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the docDB subnet group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the docDB subnet group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the docDB subnet group. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.SubnetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the docDB subnet group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the docDB subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the docDB subnet group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.docdb.SubnetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.docdb.SubnetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
