---
title: Module elasticache
title_tag: Module elasticache | Package pulumi_aws | Python SDK
linktitle: elasticache
notitle: true
---

<div class="section" id="elasticache">
<h1>elasticache<a class="headerlink" href="#elasticache" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticache"></span><dl class="py class">
<dt id="pulumi_aws.elasticache.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticache.AwaitableGetReplicationGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">AwaitableGetReplicationGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_token_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_failover_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_cache_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.AwaitableGetReplicationGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticache.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">az_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
For working with Redis (Cluster Mode Enabled) replication groups, see the
<cite>``elasticache.ReplicationGroup`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html">https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> When you change an attribute, such as <code class="docutils literal notranslate"><span class="pre">node_type</span></code>, by default
it is applied in the next maintenance window. Because of this, this provider may report
a difference in its planning phase because the actual modification has not yet taken
place. You can use the <code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> flag to instruct the service to apply the
change immediately. Using <code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> can result in a brief downtime as the server reboots.
See the AWS Docs on <a class="reference external" href="https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Modify.html">Modifying an ElastiCache Cache Cluster</a> for more information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html">Amazon ElastiCache Documentation for more information.</a>
(Available since v0.6.0)</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use <code class="docutils literal notranslate"><span class="pre">preferred_availability_zones</span></code> instead. Default: System chosen Availability Zone.</p></li>
<li><p><strong>az_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster’s region. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">single-az</span></code> or <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, default is <code class="docutils literal notranslate"><span class="pre">single-az</span></code>. If you want to choose <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code> must be greater than <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group identifier. ElastiCache converts
this name to lowercase</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">memcached</span></code> or <code class="docutils literal notranslate"><span class="pre">redis</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version number of the cache engine to be used.
See <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html">Describe Cache Engine Versions</a>
in the AWS Documentation center for supported versions</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes. See
<a class="reference external" href="https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types">Available Cache Node Types</a> for
supported node types</p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>num_cache_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.</p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the parameter group to associate
with this cache cluster</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with <code class="docutils literal notranslate"><span class="pre">replication_group_id</span></code>.</p></li>
<li><p><strong>preferred_availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code>. If you want all the nodes in the same Availability Zone, use <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.</p></li>
<li><p><strong>replication_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more VPC security groups associated
with the cache cluster</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of security group
names to associate with this cache cluster</p></li>
<li><p><strong>snapshot_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p></li>
<li><p><strong>snapshot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a snapshot from which to restore data into the new node group.  Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p></li>
<li><p><strong>snapshot_retention_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p></li>
<li><p><strong>snapshot_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00</p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the subnet group to be used
for the cache cluster.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html">Amazon ElastiCache Documentation for more information.</a>
(Available since v0.6.0)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use <code class="docutils literal notranslate"><span class="pre">preferred_availability_zones</span></code> instead. Default: System chosen Availability Zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.az_mode">
<code class="sig-name descname">az_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.az_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster’s region. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">single-az</span></code> or <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, default is <code class="docutils literal notranslate"><span class="pre">single-az</span></code>. If you want to choose <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code> must be greater than <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.cache_nodes">
<code class="sig-name descname">cache_nodes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.cache_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>.
Referenceable e.g. as <code class="docutils literal notranslate"><span class="pre">${aws_elasticache_cluster.bar.cache_nodes.0.address}</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use <code class="docutils literal notranslate"><span class="pre">preferred_availability_zones</span></code> instead. Default: System chosen Availability Zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with <code class="docutils literal notranslate"><span class="pre">replication_group_id</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.cluster_address">
<code class="sig-name descname">cluster_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.cluster_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(Memcached only) The DNS name of the cache cluster without the port appended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Group identifier. ElastiCache converts
this name to lowercase</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.configuration_endpoint">
<code class="sig-name descname">configuration_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.configuration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>(Memcached only) The configuration endpoint to allow host discovery.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">memcached</span></code> or <code class="docutils literal notranslate"><span class="pre">redis</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version number of the cache engine to be used.
See <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html">Describe Cache Engine Versions</a>
in the AWS Documentation center for supported versions</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.maintenance_window">
<code class="sig-name descname">maintenance_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.node_type">
<code class="sig-name descname">node_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the nodes. See
<a class="reference external" href="https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types">Available Cache Node Types</a> for
supported node types</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.notification_topic_arn">
<code class="sig-name descname">notification_topic_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.notification_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.num_cache_nodes">
<code class="sig-name descname">num_cache_nodes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.num_cache_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.parameter_group_name">
<code class="sig-name descname">parameter_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the parameter group to associate
with this cache cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with <code class="docutils literal notranslate"><span class="pre">replication_group_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.preferred_availability_zones">
<code class="sig-name descname">preferred_availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.preferred_availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code>. If you want all the nodes in the same Availability Zone, use <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.replication_group_id">
<code class="sig-name descname">replication_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.replication_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more VPC security groups associated
with the cache cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.security_group_names">
<code class="sig-name descname">security_group_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of security group
names to associate with this cache cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.snapshot_arns">
<code class="sig-name descname">snapshot_arns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.snapshot_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.snapshot_name">
<code class="sig-name descname">snapshot_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.snapshot_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a snapshot from which to restore data into the new node group.  Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.snapshot_retention_limit">
<code class="sig-name descname">snapshot_retention_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.snapshot_retention_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.snapshot_window">
<code class="sig-name descname">snapshot_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.snapshot_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.subnet_group_name">
<code class="sig-name descname">subnet_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the subnet group to be used
for the cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">az_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
<code class="docutils literal notranslate"><span class="pre">false</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html">Amazon ElastiCache Documentation for more information.</a>
(Available since v0.6.0)</p>
</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use <code class="docutils literal notranslate"><span class="pre">preferred_availability_zones</span></code> instead. Default: System chosen Availability Zone.</p></li>
<li><p><strong>az_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster’s region. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">single-az</span></code> or <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, default is <code class="docutils literal notranslate"><span class="pre">single-az</span></code>. If you want to choose <code class="docutils literal notranslate"><span class="pre">cross-az</span></code>, <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code> must be greater than <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>cache_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>.
Referenceable e.g. as <code class="docutils literal notranslate"><span class="pre">${aws_elasticache_cluster.bar.cache_nodes.0.address}</span></code></p></li>
<li><p><strong>cluster_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Memcached only) The DNS name of the cache cluster without the port appended.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group identifier. ElastiCache converts
this name to lowercase</p></li>
<li><p><strong>configuration_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Memcached only) The configuration endpoint to allow host discovery.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">memcached</span></code> or <code class="docutils literal notranslate"><span class="pre">redis</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Version number of the cache engine to be used.
See <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html">Describe Cache Engine Versions</a>
in the AWS Documentation center for supported versions</p>
</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The compute and memory capacity of the nodes. See
<a class="reference external" href="https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types">Available Cache Node Types</a> for
supported node types</p>
</p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>num_cache_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.</p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the parameter group to associate
with this cache cluster</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with <code class="docutils literal notranslate"><span class="pre">replication_group_id</span></code>.</p></li>
<li><p><strong>preferred_availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of <code class="docutils literal notranslate"><span class="pre">num_cache_nodes</span></code>. If you want all the nodes in the same Availability Zone, use <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.</p></li>
<li><p><strong>replication_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more VPC security groups associated
with the cache cluster</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of security group
names to associate with this cache cluster</p></li>
<li><p><strong>snapshot_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p></li>
<li><p><strong>snapshot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a snapshot from which to restore data into the new node group.  Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p></li>
<li><p><strong>snapshot_retention_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p></li>
<li><p><strong>snapshot_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00</p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the subnet group to be used
for the cache cluster.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cache_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use <code class="docutils literal notranslate"><span class="pre">preferred_availability_zones</span></code> instead. Default: System chosen Availability Zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with <code class="docutils literal notranslate"><span class="pre">replication_group_id</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_cache_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone for the cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.cache_nodes">
<code class="sig-name descname">cache_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.cache_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>.
Referenceable e.g. as <code class="docutils literal notranslate"><span class="pre">${data.aws_elasticache_cluster.bar.cache_nodes.0.address}</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.cluster_address">
<code class="sig-name descname">cluster_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.cluster_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(Memcached only) The DNS name of the cache cluster without the port appended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.configuration_endpoint">
<code class="sig-name descname">configuration_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.configuration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>(Memcached only) The configuration endpoint to allow host discovery.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cache engine.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version number of the cache engine.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.maintenance_window">
<code class="sig-name descname">maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range for when maintenance
on the cache cluster is performed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.node_type">
<code class="sig-name descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster node type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.notification_topic_arn">
<code class="sig-name descname">notification_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.notification_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>An Amazon Resource Name (ARN) of an
SNS topic that ElastiCache notifications get sent to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.num_cache_nodes">
<code class="sig-name descname">num_cache_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.num_cache_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of cache nodes that the cache cluster has.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.parameter_group_name">
<code class="sig-name descname">parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the parameter group associated with this cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number on which each of the cache nodes will
accept connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.replication_group_id">
<code class="sig-name descname">replication_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.replication_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication group to which this cache cluster belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List VPC security groups associated with the cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.security_group_names">
<code class="sig-name descname">security_group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of security group names associated with this cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.snapshot_retention_limit">
<code class="sig-name descname">snapshot_retention_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.snapshot_retention_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.snapshot_window">
<code class="sig-name descname">snapshot_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.snapshot_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of the cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.subnet_group_name">
<code class="sig-name descname">subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the subnet group associated to the cache cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags assigned to the resource</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">GetReplicationGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_token_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_failover_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_cache_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getReplicationGroup.</p>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.auth_token_enabled">
<code class="sig-name descname">auth_token_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.auth_token_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag that enables using an AuthToken (password) when issuing Redis commands.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.automatic_failover_enabled">
<code class="sig-name descname">automatic_failover_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.automatic_failover_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.configuration_endpoint_address">
<code class="sig-name descname">configuration_endpoint_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.configuration_endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration endpoint address to allow host discovery.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.member_clusters">
<code class="sig-name descname">member_clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.member_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers of all the nodes that are part of this replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.node_type">
<code class="sig-name descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster node type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.number_cache_clusters">
<code class="sig-name descname">number_cache_clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.number_cache_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of cache clusters that the replication group has.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number on which the configuration endpoint will accept connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.primary_endpoint_address">
<code class="sig-name descname">primary_endpoint_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.primary_endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint of the primary node in this node group (shard).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.replication_group_description">
<code class="sig-name descname">replication_group_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.replication_group_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.replication_group_id">
<code class="sig-name descname">replication_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.replication_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier for the replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.snapshot_retention_limit">
<code class="sig-name descname">snapshot_retention_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.snapshot_retention_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.GetReplicationGroupResult.snapshot_window">
<code class="sig-name descname">snapshot_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.GetReplicationGroupResult.snapshot_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticache.ParameterGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">ParameterGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ElastiCache parameter group resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Attempting to remove the <code class="docutils literal notranslate"><span class="pre">reserved-memory</span></code> parameter when <code class="docutils literal notranslate"><span class="pre">family</span></code> is set to <code class="docutils literal notranslate"><span class="pre">redis2.6</span></code> or <code class="docutils literal notranslate"><span class="pre">redis2.8</span></code> may show a perpetual difference in this provider due to an Elasticache API limitation. Leave that parameter configured with any value to workaround the issue.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the ElastiCache parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the ElastiCache parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ElastiCache parameter.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ElastiCache parameters to apply.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ElastiCache parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the ElastiCache parameter.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ParameterGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ElastiCache parameter group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ParameterGroup.family">
<code class="sig-name descname">family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the ElastiCache parameter group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ParameterGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ElastiCache parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ParameterGroup.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ElastiCache parameters to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ElastiCache parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the ElastiCache parameter.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.ParameterGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ParameterGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the ElastiCache parameter group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the ElastiCache parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ElastiCache parameter.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ElastiCache parameters to apply.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ElastiCache parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the ElastiCache parameter.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.ParameterGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.ParameterGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.ReplicationGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">ReplicationGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">at_rest_encryption_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_failover_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_cache_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_encryption_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ElastiCache Replication Group resource.
For working with Memcached or single primary Redis instances (Cluster Mode Disabled), see the
<cite>``elasticache.Cluster`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elasticache_cluster.html">https://www.terraform.io/docs/providers/aws/r/elasticache_cluster.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> When you change an attribute, such as <code class="docutils literal notranslate"><span class="pre">engine_version</span></code>, by
default the ElastiCache API applies it in the next maintenance window. Because
of this, this provider may report a difference in its planning phase because the
actual modification has not yet taken place. You can use the
<code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> flag to instruct the service to apply the change
immediately. Using <code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> can result in a brief downtime as
servers reboots.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>at_rest_encryption_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable encryption at rest.</p></li>
<li><p><strong>auth_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to access a password protected server. Can be specified only if <code class="docutils literal notranslate"><span class="pre">transit_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>automatic_failover_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 availability zones in which the replication group’s cache clusters will be created. The order of the availability zones in the list is not important.</p></li>
<li><p><strong>cluster_mode</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Create a native redis cluster. <code class="docutils literal notranslate"><span class="pre">automatic_failover_enabled</span></code> must be set to true. Cluster Mode documented below. Only 1 <code class="docutils literal notranslate"><span class="pre">cluster_mode</span></code> block is allowed.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cache engine to be used for the clusters in this replication group. e.g. <code class="docutils literal notranslate"><span class="pre">redis</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number of the cache engine to be used for the cache clusters in this replication group.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if <code class="docutils literal notranslate"><span class="pre">at_rest_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes in the node group.</p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>number_cache_clusters</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.</p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.</p></li>
<li><p><strong>replication_group_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-created description for the replication group.</p></li>
<li><p><strong>replication_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication group identifier. This parameter is stored as a lowercase string.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of cache security group names to associate with this replication group.</p></li>
<li><p><strong>snapshot_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p></li>
<li><p><strong>snapshot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a snapshot from which to restore data into the new node group. Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p></li>
<li><p><strong>snapshot_retention_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p></li>
<li><p><strong>snapshot_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">05:00-09:00</span></code></p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cache subnet group to be used for the replication group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource</p></li>
<li><p><strong>transit_encryption_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable encryption in transit.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_mode</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">numNodeGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicasPerNodeGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.at_rest_encryption_enabled">
<code class="sig-name descname">at_rest_encryption_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.at_rest_encryption_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable encryption at rest.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.auth_token">
<code class="sig-name descname">auth_token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.auth_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The password used to access a password protected server. Can be specified only if <code class="docutils literal notranslate"><span class="pre">transit_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.auto_minor_version_upgrade">
<code class="sig-name descname">auto_minor_version_upgrade</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.automatic_failover_enabled">
<code class="sig-name descname">automatic_failover_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.automatic_failover_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EC2 availability zones in which the replication group’s cache clusters will be created. The order of the availability zones in the list is not important.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.cluster_mode">
<code class="sig-name descname">cluster_mode</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.cluster_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a native redis cluster. <code class="docutils literal notranslate"><span class="pre">automatic_failover_enabled</span></code> must be set to true. Cluster Mode documented below. Only 1 <code class="docutils literal notranslate"><span class="pre">cluster_mode</span></code> block is allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">numNodeGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicasPerNodeGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.configuration_endpoint_address">
<code class="sig-name descname">configuration_endpoint_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.configuration_endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of the replication group configuration endpoint when cluster mode is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cache engine to be used for the clusters in this replication group. e.g. <code class="docutils literal notranslate"><span class="pre">redis</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number of the cache engine to be used for the cache clusters in this replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if <code class="docutils literal notranslate"><span class="pre">at_rest_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.maintenance_window">
<code class="sig-name descname">maintenance_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.member_clusters">
<code class="sig-name descname">member_clusters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.member_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers of all the nodes that are part of this replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.node_type">
<code class="sig-name descname">node_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the nodes in the node group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.notification_topic_arn">
<code class="sig-name descname">notification_topic_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.notification_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.number_cache_clusters">
<code class="sig-name descname">number_cache_clusters</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.number_cache_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.parameter_group_name">
<code class="sig-name descname">parameter_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.primary_endpoint_address">
<code class="sig-name descname">primary_endpoint_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.primary_endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.replication_group_description">
<code class="sig-name descname">replication_group_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.replication_group_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-created description for the replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.replication_group_id">
<code class="sig-name descname">replication_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.replication_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication group identifier. This parameter is stored as a lowercase string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.security_group_names">
<code class="sig-name descname">security_group_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cache security group names to associate with this replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.snapshot_arns">
<code class="sig-name descname">snapshot_arns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.snapshot_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.snapshot_name">
<code class="sig-name descname">snapshot_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.snapshot_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a snapshot from which to restore data into the new node group. Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.snapshot_retention_limit">
<code class="sig-name descname">snapshot_retention_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.snapshot_retention_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.snapshot_window">
<code class="sig-name descname">snapshot_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.snapshot_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">05:00-09:00</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.subnet_group_name">
<code class="sig-name descname">subnet_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cache subnet group to be used for the replication group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.ReplicationGroup.transit_encryption_enabled">
<code class="sig-name descname">transit_encryption_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.transit_encryption_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable encryption in transit.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.ReplicationGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">at_rest_encryption_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_failover_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_cache_clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_endpoint_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_retention_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_encryption_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicationGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>at_rest_encryption_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable encryption at rest.</p></li>
<li><p><strong>auth_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to access a password protected server. Can be specified only if <code class="docutils literal notranslate"><span class="pre">transit_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>automatic_failover_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of EC2 availability zones in which the replication group’s cache clusters will be created. The order of the availability zones in the list is not important.</p></li>
<li><p><strong>cluster_mode</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Create a native redis cluster. <code class="docutils literal notranslate"><span class="pre">automatic_failover_enabled</span></code> must be set to true. Cluster Mode documented below. Only 1 <code class="docutils literal notranslate"><span class="pre">cluster_mode</span></code> block is allowed.</p></li>
<li><p><strong>configuration_endpoint_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the replication group configuration endpoint when cluster mode is enabled.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cache engine to be used for the clusters in this replication group. e.g. <code class="docutils literal notranslate"><span class="pre">redis</span></code></p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number of the cache engine to be used for the cache clusters in this replication group.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if <code class="docutils literal notranslate"><span class="pre">at_rest_encryption_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code> (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>member_clusters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identifiers of all the nodes that are part of this replication group.</p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes in the node group.</p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>number_cache_clusters</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.</p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.</p></li>
<li><p><strong>primary_endpoint_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.</p></li>
<li><p><strong>replication_group_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-created description for the replication group.</p></li>
<li><p><strong>replication_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication group identifier. This parameter is stored as a lowercase string.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of cache security group names to associate with this replication group.</p></li>
<li><p><strong>snapshot_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::my_bucket/snapshot1.rdb</span></code></p></li>
<li><p><strong>snapshot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a snapshot from which to restore data into the new node group. Changing the <code class="docutils literal notranslate"><span class="pre">snapshot_name</span></code> forces a new resource.</p></li>
<li><p><strong>snapshot_retention_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a <code class="docutils literal notranslate"><span class="pre">snapshot_retention_limit</span></code> is not supported on cache.t1.micro or cache.t2.* cache nodes</p></li>
<li><p><strong>snapshot_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: <code class="docutils literal notranslate"><span class="pre">05:00-09:00</span></code></p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cache subnet group to be used for the replication group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource</p></li>
<li><p><strong>transit_encryption_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable encryption in transit.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_mode</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">numNodeGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicasPerNodeGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.ReplicationGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.ReplicationGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.ReplicationGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.SecurityGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">SecurityGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ElastiCache Security Group to control access to one or more cache
clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> ElastiCache Security Groups are for use only when working with an
ElastiCache cluster <strong>outside</strong> of a VPC. If you are using a VPC, see the
ElastiCache Subnet Group resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – description for the cache security group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the cache security group. This value is stored as a lowercase string.</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of EC2 security group names to be
authorized for ingress to the cache security group</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SecurityGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>description for the cache security group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SecurityGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the cache security group. This value is stored as a lowercase string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SecurityGroup.security_group_names">
<code class="sig-name descname">security_group_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of EC2 security group names to be
authorized for ingress to the cache security group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.SecurityGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – description for the cache security group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the cache security group. This value is stored as a lowercase string.</p></li>
<li><p><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of EC2 security group names to be
authorized for ingress to the cache security group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.SecurityGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.SecurityGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.SubnetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">SubnetGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ElastiCache Subnet Group resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> ElastiCache Subnet Groups are only for use when working with an
ElastiCache cluster <strong>inside</strong> of a VPC. If you are on EC2 Classic, see the
ElastiCache Security Group resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the cache subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the cache subnet group. Elasticache converts this name to lowercase.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC Subnet IDs for the cache subnet group</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SubnetGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the cache subnet group. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SubnetGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the cache subnet group. Elasticache converts this name to lowercase.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticache.SubnetGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC Subnet IDs for the cache subnet group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.SubnetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the cache subnet group. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the cache subnet group. Elasticache converts this name to lowercase.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of VPC Subnet IDs for the cache subnet group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticache.SubnetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticache.SubnetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.elasticache.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an Elasticache Cluster</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_id</strong> (<em>str</em>) – Group identifier.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – The tags assigned to the resource</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.elasticache.get_replication_group">
<code class="sig-prename descclassname">pulumi_aws.elasticache.</code><code class="sig-name descname">get_replication_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">replication_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticache.get_replication_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an Elasticache Replication Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>replication_group_id</strong> (<em>str</em>) – The identifier for the replication group.</p>
</dd>
</dl>
</dd></dl>

</div>
