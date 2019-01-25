<div class="section" id="module-pulumi_aws.redshift">
<span id="redshift"></span><h1>redshift<a class="headerlink" href="#module-pulumi_aws.redshift" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.redshift.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allow_version_upgrade=None</em>, <em>automated_snapshot_retention_period=None</em>, <em>availability_zone=None</em>, <em>bucket_name=None</em>, <em>cluster_identifier=None</em>, <em>cluster_parameter_group_name=None</em>, <em>cluster_public_key=None</em>, <em>cluster_revision_number=None</em>, <em>cluster_security_groups=None</em>, <em>cluster_subnet_group_name=None</em>, <em>cluster_type=None</em>, <em>cluster_version=None</em>, <em>database_name=None</em>, <em>elastic_ip=None</em>, <em>enable_logging=None</em>, <em>encrypted=None</em>, <em>endpoint=None</em>, <em>enhanced_vpc_routing=None</em>, <em>final_snapshot_identifier=None</em>, <em>iam_roles=None</em>, <em>kms_key_id=None</em>, <em>logging=None</em>, <em>master_password=None</em>, <em>master_username=None</em>, <em>node_type=None</em>, <em>number_of_nodes=None</em>, <em>owner_account=None</em>, <em>port=None</em>, <em>preferred_maintenance_window=None</em>, <em>publicly_accessible=None</em>, <em>s3_key_prefix=None</em>, <em>skip_final_snapshot=None</em>, <em>snapshot_cluster_identifier=None</em>, <em>snapshot_copy=None</em>, <em>snapshot_identifier=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Redshift Cluster Resource.</p>
<p>&gt; <strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true</li>
<li><strong>automated_snapshot_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.</li>
<li><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an existing S3 bucket where the log files are to be stored. Must be in the same region as the cluster and the cluster must have read bucket and put object permissions.
For more information on the permissions required for the bucket, please read the AWS [documentation](<a class="reference external" href="http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging">http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging</a>)</li>
<li><strong>cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cluster Identifier. Must be a lower case
string.</li>
<li><strong>cluster_parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group to be associated with this cluster.</li>
<li><strong>cluster_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key for the cluster</li>
<li><strong>cluster_revision_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The specific revision number of the database in the cluster</li>
<li><strong>cluster_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security groups to be associated with this cluster.</li>
<li><strong>cluster_subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).</li>
<li><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster type to use. Either <cite>single-node</cite> or <cite>multi-node</cite>.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the Amazon Redshift engine software that you want to deploy on the cluster.
The version selected runs on all the nodes in the cluster.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the first database to be created when the cluster is created.
If you do not provide a name, Amazon Redshift will create a default database called <cite>dev</cite>.</li>
<li><strong>elastic_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Elastic IP (EIP) address for the cluster.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[bool] enable_logging
:param pulumi.Input[bool] encrypted: If true , the data in the cluster is encrypted at rest.
:param pulumi.Input[str] endpoint: The connection endpoint
:param pulumi.Input[bool] enhanced_vpc_routing: If true , enhanced VPC routing is enabled.
:param pulumi.Input[str] final_snapshot_identifier: The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, <cite>skip_final_snapshot</cite> must be false.
:param pulumi.Input[list] iam_roles: A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.
:param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key. When specifying <cite>kms_key_id</cite>, <cite>encrypted</cite> needs to be set to true.
:param pulumi.Input[dict] logging: Logging, documented below.
:param pulumi.Input[str] master_password: Password for the master DB user.</p>
<blockquote>
<div>Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
contain at least one uppercase letter, one lowercase letter, and one number.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>master_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for the master DB user.</li>
<li><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The node type to be provisioned for the cluster.</li>
<li><strong>number_of_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.</li>
<li><strong>owner_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port number on which the cluster accepts incoming connections.
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range (in UTC) during which automated cluster maintenance can occur.
Format: ddd:hh24:mi-ddd:hh24:mi</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the cluster can be accessed from a public network. Default is <cite>true</cite>.</li>
<li><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix applied to the log file names.</li>
<li><strong>skip_final_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.</li>
<li><strong>snapshot_cluster_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster the source snapshot was created from.</li>
<li><strong>snapshot_copy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration of automatic copy of snapshots from one region to another. Documented below.</li>
<li><strong>snapshot_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the snapshot from which to create the new cluster.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.allow_version_upgrade">
<code class="descname">allow_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.allow_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.automated_snapshot_retention_period">
<code class="descname">automated_snapshot_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.automated_snapshot_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.bucket_name">
<code class="descname">bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an existing S3 bucket where the log files are to be stored. Must be in the same region as the cluster and the cluster must have read bucket and put object permissions.
For more information on the permissions required for the bucket, please read the AWS [documentation](<a class="reference external" href="http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging">http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_identifier">
<code class="descname">cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cluster Identifier. Must be a lower case
string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_parameter_group_name">
<code class="descname">cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter group to be associated with this cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_public_key">
<code class="descname">cluster_public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key for the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_revision_number">
<code class="descname">cluster_revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The specific revision number of the database in the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_security_groups">
<code class="descname">cluster_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security groups to be associated with this cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_subnet_group_name">
<code class="descname">cluster_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_type">
<code class="descname">cluster_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster type to use. Either <cite>single-node</cite> or <cite>multi-node</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the Amazon Redshift engine software that you want to deploy on the cluster.
The version selected runs on all the nodes in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the first database to be created when the cluster is created.
If you do not provide a name, Amazon Redshift will create a default database called <cite>dev</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.dns_name">
<code class="descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.elastic_ip">
<code class="descname">elastic_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.elastic_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Elastic IP (EIP) address for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true , the data in the cluster is encrypted at rest.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.enhanced_vpc_routing">
<code class="descname">enhanced_vpc_routing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.enhanced_vpc_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>If true , enhanced VPC routing is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.final_snapshot_identifier">
<code class="descname">final_snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.final_snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, <cite>skip_final_snapshot</cite> must be false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.iam_roles">
<code class="descname">iam_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <cite>kms_key_id</cite>, <cite>encrypted</cite> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.logging">
<code class="descname">logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Logging, documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.master_password">
<code class="descname">master_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.master_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the master DB user.
Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
contain at least one uppercase letter, one lowercase letter, and one number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.master_username">
<code class="descname">master_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the master DB user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.node_type">
<code class="descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The node type to be provisioned for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.number_of_nodes">
<code class="descname">number_of_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.number_of_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.owner_account">
<code class="descname">owner_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.owner_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number on which the cluster accepts incoming connections.
The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range (in UTC) during which automated cluster maintenance can occur.
Format: ddd:hh24:mi-ddd:hh24:mi</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the cluster can be accessed from a public network. Default is <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.s3_key_prefix">
<code class="descname">s3_key_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix applied to the log file names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.skip_final_snapshot">
<code class="descname">skip_final_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.skip_final_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.snapshot_cluster_identifier">
<code class="descname">snapshot_cluster_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.snapshot_cluster_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster the source snapshot was created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.snapshot_copy">
<code class="descname">snapshot_copy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.snapshot_copy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of automatic copy of snapshots from one region to another. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.snapshot_identifier">
<code class="descname">snapshot_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.snapshot_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the snapshot from which to create the new cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.Cluster.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.Cluster.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.EventSubscription">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">EventSubscription</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>enabled=None</em>, <em>event_categories=None</em>, <em>name=None</em>, <em>severity=None</em>, <em>sns_topic_arn=None</em>, <em>source_ids=None</em>, <em>source_type=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Redshift event subscription resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable the subscription. Defaults to true.</li>
<li><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event categories for a SourceType that you want to subscribe to. See <a class="reference external" href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html">https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html</a> or run <cite>aws redshift describe-event-categories</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redshift event subscription.</li>
<li><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event severity to be published by the notification subscription. Valid options are <cite>INFO</cite> or <cite>ERROR</cite>.</li>
<li><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic to send events to.</li>
<li><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.</li>
<li><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source that will be generating the events. Valid options are <cite>cluster</cite>, <cite>cluster-parameter-group</cite>, <cite>cluster-security-group</cite>, or <cite>cluster-snapshot</cite>. If not set, all sources will be subscribed to.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable the subscription. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.event_categories">
<code class="descname">event_categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of event categories for a SourceType that you want to subscribe to. See <a class="reference external" href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html">https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html</a> or run <cite>aws redshift describe-event-categories</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redshift event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.severity">
<code class="descname">severity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The event severity to be published by the notification subscription. Valid options are <cite>INFO</cite> or <cite>ERROR</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.sns_topic_arn">
<code class="descname">sns_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic to send events to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.source_ids">
<code class="descname">source_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.source_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.source_type">
<code class="descname">source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source that will be generating the events. Valid options are <cite>cluster</cite>, <cite>cluster-parameter-group</cite>, <cite>cluster-security-group</cite>, or <cite>cluster-snapshot</cite>. If not set, all sources will be subscribed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.EventSubscription.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.EventSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.EventSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>allow_version_upgrade=None</em>, <em>automated_snapshot_retention_period=None</em>, <em>availability_zone=None</em>, <em>bucket_name=None</em>, <em>cluster_parameter_group_name=None</em>, <em>cluster_public_key=None</em>, <em>cluster_revision_number=None</em>, <em>cluster_security_groups=None</em>, <em>cluster_subnet_group_name=None</em>, <em>cluster_type=None</em>, <em>cluster_version=None</em>, <em>database_name=None</em>, <em>elastic_ip=None</em>, <em>enable_logging=None</em>, <em>encrypted=None</em>, <em>endpoint=None</em>, <em>enhanced_vpc_routing=None</em>, <em>iam_roles=None</em>, <em>kms_key_id=None</em>, <em>master_username=None</em>, <em>node_type=None</em>, <em>number_of_nodes=None</em>, <em>port=None</em>, <em>preferred_maintenance_window=None</em>, <em>publicly_accessible=None</em>, <em>s3_key_prefix=None</em>, <em>vpc_id=None</em>, <em>vpc_security_group_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.allow_version_upgrade">
<code class="descname">allow_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.allow_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether major version upgrades can be applied during maintenance period</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.automated_snapshot_retention_period">
<code class="descname">automated_snapshot_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.automated_snapshot_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The backup retention period</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone of the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.bucket_name">
<code class="descname">bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the S3 bucket where the log files are to be stored</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_parameter_group_name">
<code class="descname">cluster_parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter group to be associated with this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_public_key">
<code class="descname">cluster_public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key for the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_revision_number">
<code class="descname">cluster_revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster revision number</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_security_groups">
<code class="descname">cluster_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The security groups associated with the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_subnet_group_name">
<code class="descname">cluster_subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a cluster subnet group to be associated with this cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.cluster_type">
<code class="descname">cluster_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the default database in the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.elastic_ip">
<code class="descname">elastic_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.elastic_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Elastic IP of the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.enable_logging">
<code class="descname">enable_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether cluster logging is enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the cluster data is encrypted</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.enhanced_vpc_routing">
<code class="descname">enhanced_vpc_routing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.enhanced_vpc_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enhanced VPC routing is enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.iam_roles">
<code class="descname">iam_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM roles associated to the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS encryption key associated to the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.master_username">
<code class="descname">master_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.master_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the master DB user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.node_type">
<code class="descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster node type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.number_of_nodes">
<code class="descname">number_of_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.number_of_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes in the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port the cluster responds on</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance window</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the cluster is publicly accessible</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.s3_key_prefix">
<code class="descname">s3_key_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder inside the S3 bucket where the log files are stored</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Id associated with the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC security group Ids associated with the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.redshift.GetServiceAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">GetServiceAccountResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.GetServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceAccount.</p>
<dl class="attribute">
<dt id="pulumi_aws.redshift.GetServiceAccountResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetServiceAccountResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Redshift service account in the selected region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.GetServiceAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.GetServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.redshift.ParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">ParameterGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Redshift Cluster parameter group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Redshift parameter group. Defaults to “Managed by Terraform”.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the Redshift parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redshift parameter.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Redshift parameters to apply.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.ParameterGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Redshift parameter group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.ParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the Redshift parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.ParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redshift parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.ParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Redshift parameters to apply.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.ParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.ParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">SecurityGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>ingress=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Redshift security group. Defaults to “Managed by Terraform”.</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ingress rules.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redshift security group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.SecurityGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Redshift security group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SecurityGroup.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ingress rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SecurityGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redshift security group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.SecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SnapshotCopyGrant">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">SnapshotCopyGrant</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>kms_key_id=None</em>, <em>snapshot_copy_grant_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.</p>
<p>Note that the grant must exist in the destination region, and not in the region of the cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.</li>
<li><strong>snapshot_copy_grant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for identifying the grant.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.SnapshotCopyGrant.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SnapshotCopyGrant.snapshot_copy_grant_name">
<code class="descname">snapshot_copy_grant_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant.snapshot_copy_grant_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for identifying the grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SnapshotCopyGrant.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.SnapshotCopyGrant.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SnapshotCopyGrant.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SnapshotCopyGrant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.redshift.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Redshift Subnet group. Defaults to “Managed by Terraform”.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redshift Subnet group.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of VPC subnet IDs.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.redshift.SubnetGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Redshift Subnet group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SubnetGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redshift Subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.redshift.SubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.redshift.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.redshift.get_cluster">
<code class="descclassname">pulumi_aws.redshift.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>cluster_identifier=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific redshift cluster.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.redshift.get_service_account">
<code class="descclassname">pulumi_aws.redshift.</code><code class="descname">get_service_account</code><span class="sig-paren">(</span><em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.redshift.get_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Account ID of the [AWS Redshift Service Account](<a class="reference external" href="http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging">http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging</a>)
in a given region for the purpose of allowing Redshift to store audit data in S3.</p>
</dd></dl>

</div>
