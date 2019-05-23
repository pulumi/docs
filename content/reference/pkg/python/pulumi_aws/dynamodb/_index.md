<div class="section" id="module-pulumi_aws.dynamodb">
<span id="dynamodb"></span><h1>dynamodb<a class="headerlink" href="#module-pulumi_aws.dynamodb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.dynamodb.GetTableResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.dynamodb.</code><code class="descname">GetTableResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>attributes=None</em>, <em>billing_mode=None</em>, <em>global_secondary_indexes=None</em>, <em>hash_key=None</em>, <em>local_secondary_indexes=None</em>, <em>name=None</em>, <em>point_in_time_recovery=None</em>, <em>range_key=None</em>, <em>read_capacity=None</em>, <em>server_side_encryption=None</em>, <em>stream_arn=None</em>, <em>stream_enabled=None</em>, <em>stream_label=None</em>, <em>stream_view_type=None</em>, <em>tags=None</em>, <em>ttl=None</em>, <em>write_capacity=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GetTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTable.</p>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GetTableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GetTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.dynamodb.GlobalTable">
<em class="property">class </em><code class="descclassname">pulumi_aws.dynamodb.</code><code class="descname">GlobalTable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>replicas=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.</p>
<blockquote>
<div>Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the <a class="reference external" href="http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html">AWS DynamoDB Global Table Requirements</a> for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the global table. Must match underlying DynamoDB Table names in all regions.</li>
<li><strong>replicas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Underlying DynamoDB Table. At least 1 replica must be defined. See below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the DynamoDB Global Table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the global table. Must match underlying DynamoDB Table names in all regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.GlobalTable.replicas">
<code class="descname">replicas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.replicas" title="Permalink to this definition">¶</a></dt>
<dd><p>Underlying DynamoDB Table. At least 1 replica must be defined. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.GlobalTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.GlobalTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.GlobalTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.Table">
<em class="property">class </em><code class="descclassname">pulumi_aws.dynamodb.</code><code class="descname">Table</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attributes=None</em>, <em>billing_mode=None</em>, <em>global_secondary_indexes=None</em>, <em>hash_key=None</em>, <em>local_secondary_indexes=None</em>, <em>name=None</em>, <em>point_in_time_recovery=None</em>, <em>range_key=None</em>, <em>read_capacity=None</em>, <em>server_side_encryption=None</em>, <em>stream_enabled=None</em>, <em>stream_view_type=None</em>, <em>tags=None</em>, <em>ttl=None</em>, <em>write_capacity=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DynamoDB table resource</p>
<blockquote>
<div><strong>Note:</strong> It is recommended to use <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> <cite>``ignore_changes`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#ignore_changes">https://www.terraform.io/docs/configuration/resources.html#ignore_changes</a>&gt;`_ for <code class="docutils literal notranslate"><span class="pre">read_capacity</span></code> and/or <code class="docutils literal notranslate"><span class="pre">write_capacity</span></code> if there’s <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html">autoscaling policy</a> attached to the table.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested attribute definitions. Only required for <code class="docutils literal notranslate"><span class="pre">hash_key</span></code> and <code class="docutils literal notranslate"><span class="pre">range_key</span></code> attributes. Each attribute has two properties:</li>
<li><strong>billing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how you are charged for read and write throughput and how you manage capacity. The valid values are <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> and <code class="docutils literal notranslate"><span class="pre">PAY_PER_REQUEST</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</li>
<li><strong>global_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.</li>
<li><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the hash key in the index; must be
defined as an attribute in the resource.</li>
<li><strong>local_secondary_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describe an LSI on the table;
these can only be allocated <em>at creation</em> so you cannot change this
definition after you have created the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index</li>
<li><strong>point_in_time_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Point-in-time recovery options.</li>
<li><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the range key; must be defined</li>
<li><strong>read_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</li>
<li><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn’t specified.</li>
<li><strong>stream_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Streams are to be enabled (true) or disabled (false).</li>
<li><strong>stream_view_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When an item in the table is modified, StreamViewType determines what information is written to the table’s stream. Valid values are <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">OLD_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_AND_OLD_IMAGES</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to populate on the created table.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines ttl, has two properties, and can only be specified once:</li>
<li><strong>write_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The arn of the table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested attribute definitions. Only required for <code class="docutils literal notranslate"><span class="pre">hash_key</span></code> and <code class="docutils literal notranslate"><span class="pre">range_key</span></code> attributes. Each attribute has two properties:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.billing_mode">
<code class="descname">billing_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.billing_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how you are charged for read and write throughput and how you manage capacity. The valid values are <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> and <code class="docutils literal notranslate"><span class="pre">PAY_PER_REQUEST</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.global_secondary_indexes">
<code class="descname">global_secondary_indexes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.global_secondary_indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.hash_key">
<code class="descname">hash_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.hash_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the hash key in the index; must be
defined as an attribute in the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.local_secondary_indexes">
<code class="descname">local_secondary_indexes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.local_secondary_indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>Describe an LSI on the table;
these can only be allocated <em>at creation</em> so you cannot change this
definition after you have created the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the index</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.point_in_time_recovery">
<code class="descname">point_in_time_recovery</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.point_in_time_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Point-in-time recovery options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.range_key">
<code class="descname">range_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.range_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the range key; must be defined</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.read_capacity">
<code class="descname">read_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.read_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.server_side_encryption">
<code class="descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn’t specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_arn">
<code class="descname">stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Table Stream. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_enabled">
<code class="descname">stream_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Streams are to be enabled (true) or disabled (false).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_label">
<code class="descname">stream_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_label" title="Permalink to this definition">¶</a></dt>
<dd><p>A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when <code class="docutils literal notranslate"><span class="pre">stream_enabled</span> <span class="pre">=</span> <span class="pre">true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.stream_view_type">
<code class="descname">stream_view_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.stream_view_type" title="Permalink to this definition">¶</a></dt>
<dd><p>When an item in the table is modified, StreamViewType determines what information is written to the table’s stream. Valid values are <code class="docutils literal notranslate"><span class="pre">KEYS_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">OLD_IMAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">NEW_AND_OLD_IMAGES</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to populate on the created table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines ttl, has two properties, and can only be specified once:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.Table.write_capacity">
<code class="descname">write_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.Table.write_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.Table.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.Table.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.TableItem">
<em class="property">class </em><code class="descclassname">pulumi_aws.dynamodb.</code><code class="descname">TableItem</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>hash_key=None</em>, <em>item=None</em>, <em>range_key=None</em>, <em>table_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DynamoDB table item resource</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.</dt>
<dd>You should perform <strong>regular backups</strong> of all data in the table, see <a class="reference external" href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html">AWS docs for more</a>.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>hash_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hash key to use for lookups and identification of the item</li>
<li><strong>item</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</li>
<li><strong>range_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range key to use for lookups and identification of the item. Required if there is range key defined in the table.</li>
<li><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table to contain the item.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.hash_key">
<code class="descname">hash_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.hash_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Hash key to use for lookups and identification of the item</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.item">
<code class="descname">item</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.item" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.range_key">
<code class="descname">range_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.range_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Range key to use for lookups and identification of the item. Required if there is range key defined in the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dynamodb.TableItem.table_name">
<code class="descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the table to contain the item.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dynamodb.TableItem.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.TableItem.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.TableItem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dynamodb.get_table">
<code class="descclassname">pulumi_aws.dynamodb.</code><code class="descname">get_table</code><span class="sig-paren">(</span><em>name=None</em>, <em>server_side_encryption=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dynamodb.get_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a DynamoDB table.</p>
</dd></dl>

</div>
