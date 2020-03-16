---
title: Module dynamodb
title_tag: Module dynamodb | Package pulumi_aws | Python SDK
linktitle: dynamodb
notitle: true
---

<div class="section" id="dynamodb">
<h1>dynamodb<a class="headerlink" href="#dynamodb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.dynamodb"></span><dl class="class">
<dt id="pulumi_aws.dynamodb.AwaitableGetTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">AwaitableGetTableResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">billing_mode=None</em>, <em class="sig-param">global_secondary_indexes=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">local_secondary_indexes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">point_in_time_recovery=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">read_capacity=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">stream_arn=None</em>, <em class="sig-param">stream_enabled=None</em>, <em class="sig-param">stream_label=None</em>, <em class="sig-param">stream_view_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">write_capacity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.AwaitableGetTableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.dynamodb.GetTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">GetTableResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">billing_mode=None</em>, <em class="sig-param">global_secondary_indexes=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">local_secondary_indexes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">point_in_time_recovery=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">read_capacity=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">stream_arn=None</em>, <em class="sig-param">stream_enabled=None</em>, <em class="sig-param">stream_label=None</em>, <em class="sig-param">stream_view_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">write_capacity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GetTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTable.</p>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GetTableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GetTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.dynamodb.GlobalTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">GlobalTable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">replicas=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.</p>
<blockquote>
<div><p>Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the <a class="reference external" href="http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html">AWS DynamoDB Global Table Requirements</a> for more information.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_global_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_global_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the global table. Must match underlying DynamoDB Table names in all regions.</p></li>
<li><p><strong>replicas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Underlying DynamoDB Table. At least 1 replica must be defined. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>replicas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region name of replica DynamoDB Table. e.g. <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code></p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the DynamoDB Global Table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the global table. Must match underlying DynamoDB Table names in all regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.replicas">
<code class="sig-name descname">replicas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.replicas" title="Permalink to this definition">¶</a></dt>
<dd><p>Underlying DynamoDB Table. At least 1 replica must be defined. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS region name of replica DynamoDB Table. e.g. <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.GlobalTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">replicas=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalTable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the DynamoDB Global Table</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the global table. Must match underlying DynamoDB Table names in all regions.</p></li>
<li><p><strong>replicas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Underlying DynamoDB Table. At least 1 replica must be defined. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>replicas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region name of replica DynamoDB Table. e.g. <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.GlobalTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.GlobalTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">billing_mode=None</em>, <em class="sig-param">global_secondary_indexes=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">local_secondary_indexes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">point_in_time_recovery=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">read_capacity=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">stream_enabled=None</em>, <em class="sig-param">stream_view_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">write_capacity=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DynamoDB table resource</p>
<blockquote>
<div><p><strong>Note:</strong> It is recommended to use <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> <cite>``ignore_changes`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#ignore_changes">https://www.terraform.io/docs/configuration/resources.html#ignore_changes</a>&gt;`_ for <code class="docutils literal notranslate"><span class="pre">read_capacity</span></code> and/or <code class="docutils literal notranslate"><span class="pre">write_capacity</span></code> if there’s <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html">autoscaling policy</a> attached to the table.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested attribute definitions. Only required for <code class="docutils literal notranslate"><span class="pre">hash_key</span></code> and <code class="docutils literal notranslate"><span class="pre">range_key</span></code> attributes. Each attribute has two properties:</p></li>
<li><p><strong>billing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how you are charged for read and write throughput and how you manage capacity. The valid values are <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> and <code class="docutils literal notranslate"><span class="pre">PAY_PER_REQUEST</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p></li>
<li><p><strong>global_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.</p></li>
<li><p><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the hash key in the index; must be
defined as an attribute in the resource.</p></li>
<li><p><strong>local_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe an LSI on the table;
these can only be allocated <em>at creation</em> so you cannot change this
definition after you have created the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index</p></li>
<li><p><strong>point_in_time_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Point-in-time recovery options.</p></li>
<li><p><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the range key; must be defined</p></li>
<li><p><strong>read_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn’t specified.</p></li>
<li><p><strong>stream_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Streams are to be enabled (true) or disabled (false).</p></li>
<li><p><strong>stream_view_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When an item in the table is modified, StreamViewType determines what information is written to the table’s stream. Valid values are <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">OLD_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_AND_OLD_IMAGES</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to populate on the created table.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines ttl, has two properties, and can only be specified once:</p></li>
<li><p><strong>write_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Attribute type, which must be a scalar type: <code class="docutils literal notranslate"><span class="pre">S</span></code>, <code class="docutils literal notranslate"><span class="pre">N</span></code>, or <code class="docutils literal notranslate"><span class="pre">B</span></code> for (S)tring, (N)umber or (B)inary data</p></li>
</ul>
<p>The <strong>global_secondary_indexes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the hash key in the index; must be
defined as an attribute in the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the range key; must be defined</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
</ul>
<p>The <strong>local_secondary_indexes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the range key; must be defined</p></li>
</ul>
<p>The <strong>point_in_time_recovery</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, <code class="docutils literal notranslate"><span class="pre">alias/aws/dynamodb</span></code>.</p></li>
</ul>
<p>The <strong>ttl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the table attribute to store the TTL timestamp in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The arn of the table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.attributes">
<code class="sig-name descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested attribute definitions. Only required for <code class="docutils literal notranslate"><span class="pre">hash_key</span></code> and <code class="docutils literal notranslate"><span class="pre">range_key</span></code> attributes. Each attribute has two properties:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Attribute type, which must be a scalar type: <code class="docutils literal notranslate"><span class="pre">S</span></code>, <code class="docutils literal notranslate"><span class="pre">N</span></code>, or <code class="docutils literal notranslate"><span class="pre">B</span></code> for (S)tring, (N)umber or (B)inary data</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.billing_mode">
<code class="sig-name descname">billing_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.billing_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how you are charged for read and write throughput and how you manage capacity. The valid values are <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> and <code class="docutils literal notranslate"><span class="pre">PAY_PER_REQUEST</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.global_secondary_indexes">
<code class="sig-name descname">global_secondary_indexes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.global_secondary_indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the hash key in the index; must be
defined as an attribute in the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the range key; must be defined</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.hash_key">
<code class="sig-name descname">hash_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.hash_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the hash key in the index; must be
defined as an attribute in the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.local_secondary_indexes">
<code class="sig-name descname">local_secondary_indexes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.local_secondary_indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>Describe an LSI on the table;
these can only be allocated <em>at creation</em> so you cannot change this
definition after you have created the resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the range key; must be defined</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the index</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.point_in_time_recovery">
<code class="sig-name descname">point_in_time_recovery</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.point_in_time_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Point-in-time recovery options.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.range_key">
<code class="sig-name descname">range_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.range_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the range key; must be defined</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.read_capacity">
<code class="sig-name descname">read_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.read_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn’t specified.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, <code class="docutils literal notranslate"><span class="pre">alias/aws/dynamodb</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_arn">
<code class="sig-name descname">stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Table Stream. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_enabled">
<code class="sig-name descname">stream_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Streams are to be enabled (true) or disabled (false).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_label">
<code class="sig-name descname">stream_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_label" title="Permalink to this definition">¶</a></dt>
<dd><p>A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_view_type">
<code class="sig-name descname">stream_view_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_view_type" title="Permalink to this definition">¶</a></dt>
<dd><p>When an item in the table is modified, StreamViewType determines what information is written to the table’s stream. Valid values are <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">OLD_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_AND_OLD_IMAGES</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to populate on the created table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines ttl, has two properties, and can only be specified once:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the table attribute to store the TTL timestamp in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.write_capacity">
<code class="sig-name descname">write_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.write_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">billing_mode=None</em>, <em class="sig-param">global_secondary_indexes=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">local_secondary_indexes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">point_in_time_recovery=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">read_capacity=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">stream_arn=None</em>, <em class="sig-param">stream_enabled=None</em>, <em class="sig-param">stream_label=None</em>, <em class="sig-param">stream_view_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">write_capacity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The arn of the table</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested attribute definitions. Only required for <code class="docutils literal notranslate"><span class="pre">hash_key</span></code> and <code class="docutils literal notranslate"><span class="pre">range_key</span></code> attributes. Each attribute has two properties:</p></li>
<li><p><strong>billing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how you are charged for read and write throughput and how you manage capacity. The valid values are <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> and <code class="docutils literal notranslate"><span class="pre">PAY_PER_REQUEST</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p></li>
<li><p><strong>global_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.</p></li>
<li><p><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the hash key in the index; must be
defined as an attribute in the resource.</p></li>
<li><p><strong>local_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe an LSI on the table;
these can only be allocated <em>at creation</em> so you cannot change this
definition after you have created the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index</p></li>
<li><p><strong>point_in_time_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Point-in-time recovery options.</p></li>
<li><p><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the range key; must be defined</p></li>
<li><p><strong>read_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn’t specified.</p></li>
<li><p><strong>stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Table Stream. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><strong>stream_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Streams are to be enabled (true) or disabled (false).</p></li>
<li><p><strong>stream_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><strong>stream_view_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When an item in the table is modified, StreamViewType determines what information is written to the table’s stream. Valid values are <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">OLD_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_AND_OLD_IMAGES</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to populate on the created table.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines ttl, has two properties, and can only be specified once:</p></li>
<li><p><strong>write_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Attribute type, which must be a scalar type: <code class="docutils literal notranslate"><span class="pre">S</span></code>, <code class="docutils literal notranslate"><span class="pre">N</span></code>, or <code class="docutils literal notranslate"><span class="pre">B</span></code> for (S)tring, (N)umber or (B)inary data</p></li>
</ul>
<p>The <strong>global_secondary_indexes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the hash key in the index; must be
defined as an attribute in the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the range key; must be defined</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p></li>
</ul>
<p>The <strong>local_secondary_indexes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonKeyAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Only required with <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code> or <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
where <code class="docutils literal notranslate"><span class="pre">ALL</span></code> projects every attribute into the index, <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>
projects just the hash and range key into the index, and <code class="docutils literal notranslate"><span class="pre">INCLUDE</span></code>
projects only the keys specified in the _non_key<em>attributes</em>
parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the range key; must be defined</p></li>
</ul>
<p>The <strong>point_in_time_recovery</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, <code class="docutils literal notranslate"><span class="pre">alias/aws/dynamodb</span></code>.</p></li>
</ul>
<p>The <strong>ttl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the table attribute to store the TTL timestamp in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the <code class="docutils literal notranslate"><span class="pre">point_in_time_recovery</span></code> block is not provided then this defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.TableItem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">TableItem</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">item=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DynamoDB table item resource</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.</dt><dd><p>You should perform <strong>regular backups</strong> of all data in the table, see <a class="reference external" href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html">AWS docs for more</a>.</p>
</dd>
</dl>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table_item.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table_item.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hash key to use for lookups and identification of the item</p></li>
<li><p><strong>item</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p></li>
<li><p><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range key to use for lookups and identification of the item. Required if there is range key defined in the table.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table to contain the item.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.hash_key">
<code class="sig-name descname">hash_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.hash_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Hash key to use for lookups and identification of the item</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.item">
<code class="sig-name descname">item</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.item" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.range_key">
<code class="sig-name descname">range_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.range_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Range key to use for lookups and identification of the item. Required if there is range key defined in the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the table to contain the item.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.TableItem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">hash_key=None</em>, <em class="sig-param">item=None</em>, <em class="sig-param">range_key=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TableItem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hash key to use for lookups and identification of the item</p></li>
<li><p><strong>item</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p></li>
<li><p><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range key to use for lookups and identification of the item. Required if there is range key defined in the table.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table to contain the item.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.TableItem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.TableItem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.dynamodb.get_table">
<code class="sig-prename descclassname">pulumi_aws.dynamodb.</code><code class="sig-name descname">get_table</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.get_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a DynamoDB table.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/dynamodb_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/dynamodb_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the DynamoDB table.</p>
</dd>
</dl>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

</div>
