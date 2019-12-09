---
title: Module dax
title_tag: Module dax | Package pulumi_aws | Python SDK
linktitle: dax
notitle: true
---

<div class="section" id="dax">
<h1>dax<a class="headerlink" href="#dax" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.dax"></span><dl class="class">
<dt id="pulumi_aws.dax.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dax.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">iam_role_arn=None</em>, <em class="sig-param">maintenance_window=None</em>, <em class="sig-param">node_type=None</em>, <em class="sig-param">notification_topic_arn=None</em>, <em class="sig-param">parameter_group_name=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">subnet_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Cluster resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Availability Zones in which the
nodes will be created</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group identifier. DAX converts this name to
lowercase</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the cluster</p></li>
<li><p><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role’s
permissions to access DynamoDB on your behalf</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when
maintenance on the cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code>
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
<code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types</p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the parameter group to associate
with this DAX cluster</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more VPC security groups associated
with the cluster</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options</p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the subnet group to be used for the
cluster</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable encryption at rest. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the DAX cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Availability Zones in which the
nodes will be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.cluster_address">
<code class="sig-name descname">cluster_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.cluster_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the DAX cluster without the port appended</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Group identifier. DAX converts this name to
lowercase</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.configuration_endpoint">
<code class="sig-name descname">configuration_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.configuration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.iam_role_arn">
<code class="sig-name descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role’s
permissions to access DynamoDB on your behalf</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.maintenance_window">
<code class="sig-name descname">maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the weekly time range for when
maintenance on the cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code>
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
<code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.node_type">
<code class="sig-name descname">node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.nodes">
<code class="sig-name descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and
<code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>. Referenceable e.g. as
<code class="docutils literal notranslate"><span class="pre">${aws_dax_cluster.test.nodes.0.address}</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port used by the configuration endpoint</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.notification_topic_arn">
<code class="sig-name descname">notification_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.notification_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.parameter_group_name">
<code class="sig-name descname">parameter_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.parameter_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the parameter group to associate
with this DAX cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used by the configuration endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more VPC security groups associated
with the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypt at rest options</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable encryption at rest. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.subnet_group_name">
<code class="sig-name descname">subnet_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.subnet_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the subnet group to be used for the
cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">cluster_address=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">configuration_endpoint=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">iam_role_arn=None</em>, <em class="sig-param">maintenance_window=None</em>, <em class="sig-param">node_type=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">notification_topic_arn=None</em>, <em class="sig-param">parameter_group_name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">subnet_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the DAX cluster</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Availability Zones in which the
nodes will be created</p></li>
<li><p><strong>cluster_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name of the DAX cluster without the port appended</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group identifier. DAX converts this name to
lowercase</p></li>
<li><p><strong>configuration_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the cluster</p></li>
<li><p><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role’s
permissions to access DynamoDB on your behalf</p></li>
<li><p><strong>maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the weekly time range for when
maintenance on the cluster is performed. The format is <code class="docutils literal notranslate"><span class="pre">ddd:hh24:mi-ddd:hh24:mi</span></code>
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
<code class="docutils literal notranslate"><span class="pre">sun:05:00-sun:09:00</span></code></p></li>
<li><p><strong>node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node objects including <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">address</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code> and
<code class="docutils literal notranslate"><span class="pre">availability_zone</span></code>. Referenceable e.g. as
<code class="docutils literal notranslate"><span class="pre">${aws_dax_cluster.test.nodes.0.address}</span></code></p></li>
<li><p><strong>notification_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
<code class="docutils literal notranslate"><span class="pre">arn:aws:sns:us-east-1:012345678999:my_sns_topic</span></code></p></li>
<li><p><strong>parameter_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the parameter group to associate
with this DAX cluster</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used by the configuration endpoint</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more VPC security groups associated
with the cluster</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options</p></li>
<li><p><strong>subnet_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the subnet group to be used for the
cluster</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port used by the configuration endpoint</p></li>
</ul>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable encryption at rest. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.ParameterGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dax.</code><code class="sig-name descname">ParameterGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Parameter Group resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Required) The value for the parameter.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parameters of the parameter group.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the parameter group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_parameter_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_parameter_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.ParameterGroup.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameters of the parameter group.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the parameter group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.ParameterGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ParameterGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the parameter group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter group.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parameters of the parameter group.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the parameter group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_parameter_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_parameter_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.ParameterGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.ParameterGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.ParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.SubnetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dax.</code><code class="sig-name descname">SubnetGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DAX Subnet Group resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the subnet group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet group.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs for the subnet group.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_subnet_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_subnet_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs for the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dax.SubnetGroup.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID of the subnet group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.SubnetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the subnet group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet group.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs for the subnet group.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC ID of the subnet group.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_subnet_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_subnet_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dax.SubnetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dax.SubnetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dax.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
