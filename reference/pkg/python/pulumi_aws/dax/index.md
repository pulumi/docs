<div class="section" id="module-pulumi_aws.dax">
<span id="dax"></span><h1>dax<a class="headerlink" href="#module-pulumi_aws.dax" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.dax.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.dax.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zones=None</em>, <em>cluster_name=None</em>, <em>description=None</em>, <em>iam_role_arn=None</em>, <em>maintenance_window=None</em>, <em>node_type=None</em>, <em>notification_topic_arn=None</em>, <em>parameter_group_name=None</em>, <em>replication_factor=None</em>, <em>security_group_ids=None</em>, <em>server_side_encryption=None</em>, <em>subnet_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Cluster resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Availability Zones in which the
nodes will be created</li>
<li><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group identifier. DAX converts this name to
lowercase</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the cluster</li>
<li><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role’s
permissions to access DynamoDB on your behalf</li>
<li><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when
maintenance on the cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code>
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
<code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></li>
<li><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types</li>
<li><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></li>
<li><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the parameter group to associate
with this DAX cluster</li>
<li><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas</li>
<li><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more VPC security groups associated
with the cluster</li>
<li><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options</li>
<li><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the subnet group to be used for the
cluster</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the DAX cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Availability Zones in which the
nodes will be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.cluster_address">
<code class="descname">cluster_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.cluster_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the DAX cluster without the port appended</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.cluster_name">
<code class="descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Group identifier. DAX converts this name to
lowercase</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.configuration_endpoint">
<code class="descname">configuration_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.configuration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.iam_role_arn">
<code class="descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role’s
permissions to access DynamoDB on your behalf</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.maintenance_window">
<code class="descname">maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range for when
maintenance on the cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code>
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
<code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.node_type">
<code class="descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.nodes">
<code class="descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and
<code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>. Referenceable e.g. as
<code class="docutils literal notranslate"><span class="pre">${aws_dax_cluster.test.nodes.0.address}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.notification_topic_arn">
<code class="descname">notification_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.notification_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.parameter_group_name">
<code class="descname">parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the parameter group to associate
with this DAX cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used by the configuration endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.replication_factor">
<code class="descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more VPC security groups associated
with the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.server_side_encryption">
<code class="descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypt at rest options</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.subnet_group_name">
<code class="descname">subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the subnet group to be used for the
cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.ParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.dax.</code><code class="descname">ParameterGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Parameter Group resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the parameter.</li>
<li><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Required) The value for the parameter.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parameters of the parameter group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameters of the parameter group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.ParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.ParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.dax.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>subnet_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Subnet Group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the subnet group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet group.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs for the subnet group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs for the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID of the subnet group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
