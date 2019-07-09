---
---

<div class="section" id="module-pulumi_aws.glue">
<span id="glue"></span><h1>glue<a class="headerlink" href="#module-pulumi_aws.glue" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.glue.CatalogDatabase">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">CatalogDatabase</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>catalog_id=None</em>, <em>description=None</em>, <em>location_uri=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Catalog Database Resource. You can refer to the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html">Glue Developer Guide</a> for a full explanation of the Glue Data Catalog functionality</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the database.</li>
<li><strong>location_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the database (for example, an HDFS path).</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of key-value pairs that define parameters and properties of the database.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.catalog_id">
<code class="descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.location_uri">
<code class="descname">location_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.location_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the database (for example, an HDFS path).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key-value pairs that define parameters and properties of the database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogDatabase.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogDatabase.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">CatalogTable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>catalog_id=None</em>, <em>database_name=None</em>, <em>description=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>parameters=None</em>, <em>partition_keys=None</em>, <em>retention=None</em>, <em>storage_descriptor=None</em>, <em>table_type=None</em>, <em>view_expanded_text=None</em>, <em>view_original_text=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Catalog Table Resource. You can refer to the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html">Glue Developer Guide</a> for a full explanation of the Glue Data Catalog functionality.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the table.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SerDe.</li>
<li><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner of the table.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of initialization parameters for the SerDe, in key-value form.</li>
<li><strong>partition_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</li>
<li><strong>retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention time for this table.</li>
<li><strong>storage_descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
</li>
<li><strong>table_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</li>
<li><strong>view_expanded_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the expanded text of the view; otherwise null.</li>
<li><strong>view_original_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the original text of the view; otherwise null.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.catalog_id">
<code class="descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SerDe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Owner of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of initialization parameters for the SerDe, in key-value form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.partition_keys">
<code class="descname">partition_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.partition_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.retention">
<code class="descname">retention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.retention" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention time for this table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.storage_descriptor">
<code class="descname">storage_descriptor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.storage_descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.table_type">
<code class="descname">table_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.table_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_expanded_text">
<code class="descname">view_expanded_text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_expanded_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the expanded text of the view; otherwise null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_original_text">
<code class="descname">view_original_text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_original_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the original text of the view; otherwise null.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">Classifier</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>grok_classifier=None</em>, <em>json_classifier=None</em>, <em>name=None</em>, <em>xml_classifier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Classifier resource.</p>
<blockquote>
<div><strong>NOTE:</strong> It is only valid to create one type of classifier (grok, JSON, or XML). Changing classifier types will recreate the classifier.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>grok_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier that uses grok patterns. Defined below.</li>
<li><strong>json_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for JSON content. Defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the classifier.</li>
<li><strong>xml_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for XML content. Defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.grok_classifier">
<code class="descname">grok_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.grok_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier that uses grok patterns. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.json_classifier">
<code class="descname">json_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.json_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for JSON content. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the classifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.xml_classifier">
<code class="descname">xml_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.xml_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for XML content. Defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Classifier.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">Connection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>catalog_id=None</em>, <em>connection_properties=None</em>, <em>connection_type=None</em>, <em>description=None</em>, <em>match_criterias=None</em>, <em>name=None</em>, <em>physical_connection_requirements=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Connection resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</li>
<li><strong>connection_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key-value pairs used as parameters for this connection.</li>
<li><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the connection.</li>
<li><strong>match_criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of criteria that can be used in selecting this connection.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</li>
<li><strong>physical_connection_requirements</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.catalog_id">
<code class="descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.connection_properties">
<code class="descname">connection_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key-value pairs used as parameters for this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.connection_type">
<code class="descname">connection_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.match_criterias">
<code class="descname">match_criterias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.match_criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of criteria that can be used in selecting this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.physical_connection_requirements">
<code class="descname">physical_connection_requirements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.physical_connection_requirements" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Connection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">Crawler</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>classifiers=None</em>, <em>configuration=None</em>, <em>database_name=None</em>, <em>description=None</em>, <em>dynamodb_targets=None</em>, <em>jdbc_targets=None</em>, <em>name=None</em>, <em>role=None</em>, <em>s3_targets=None</em>, <em>schedule=None</em>, <em>schema_change_policy=None</em>, <em>security_configuration=None</em>, <em>table_prefix=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Crawler. More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">AWS Glue Developer Guide</a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>classifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of configuration information.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Glue database where results are written.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the crawler.</li>
<li><strong>dynamodb_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested DynamoDB target arguments. See below.</li>
<li><strong>jdbc_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested JBDC target arguments. See below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the crawler.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</li>
<li><strong>s3_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List nested Amazon S3 target arguments. See below.</li>
<li><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</li>
<li><strong>schema_change_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy for the crawler’s update and deletion behavior.</li>
<li><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of Security Configuration to be used by the crawler</li>
<li><strong>table_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table prefix used for catalog tables that are created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the crawler</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.classifiers">
<code class="descname">classifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.classifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string of configuration information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Glue database where results are written.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the crawler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.dynamodb_targets">
<code class="descname">dynamodb_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.dynamodb_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested DynamoDB target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.jdbc_targets">
<code class="descname">jdbc_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.jdbc_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested JBDC target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the crawler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.s3_targets">
<code class="descname">s3_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.s3_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List nested Amazon S3 target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.schedule">
<code class="descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.schema_change_policy">
<code class="descname">schema_change_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schema_change_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy for the crawler’s update and deletion behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.security_configuration">
<code class="descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of Security Configuration to be used by the crawler</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.table_prefix">
<code class="descname">table_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.table_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The table prefix used for catalog tables that are created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Crawler.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.GetScriptResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">GetScriptResult</code><span class="sig-paren">(</span><em>dag_edges=None</em>, <em>dag_nodes=None</em>, <em>language=None</em>, <em>python_script=None</em>, <em>scala_code=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScript.</p>
<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.python_script">
<code class="descname">python_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.python_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Python script generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">PYTHON</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.scala_code">
<code class="descname">scala_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.scala_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scala code generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">SCALA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.glue.Job">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocated_capacity=None</em>, <em>command=None</em>, <em>connections=None</em>, <em>default_arguments=None</em>, <em>description=None</em>, <em>execution_property=None</em>, <em>max_capacity=None</em>, <em>max_retries=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>security_configuration=None</em>, <em>timeout=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Job resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocated_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</li>
<li><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The command of the job. Defined below.</li>
<li><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of connections used for this job.</li>
<li><strong>default_arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the job.</li>
<li><strong>execution_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Execution property of the job. Defined below.</li>
<li><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</li>
<li><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times to retry this job if it fails.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code></li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role associated with this job.</li>
<li><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Security Configuration to be associated with the job.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The job timeout in minutes. The default is 2880 minutes (48 hours).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Job.allocated_capacity">
<code class="descname">allocated_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.allocated_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.command">
<code class="descname">command</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.command" title="Permalink to this definition">¶</a></dt>
<dd><p>The command of the job. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.connections">
<code class="descname">connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of connections used for this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.default_arguments">
<code class="descname">default_arguments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.default_arguments" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.execution_property">
<code class="descname">execution_property</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.execution_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Execution property of the job. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.max_capacity">
<code class="descname">max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.max_retries">
<code class="descname">max_retries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times to retry this job if it fails.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role associated with this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.security_configuration">
<code class="descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Security Configuration to be associated with the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The job timeout in minutes. The default is 2880 minutes (48 hours).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Job.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Job.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">SecurityConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>encryption_configuration=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Security Configuration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing encryption configuration. Detailed below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the security configuration.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.encryption_configuration">
<code class="descname">encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing encryption configuration. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the security configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger">
<em class="property">class </em><code class="descclassname">pulumi_aws.glue.</code><code class="descname">Trigger</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>actions=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>predicate=None</em>, <em>schedule=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Trigger resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of actions initiated by this trigger when it fires. Defined below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the new trigger.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the trigger.</li>
<li><strong>predicate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</li>
<li><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.actions">
<code class="descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of actions initiated by this trigger when it fires. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the new trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.predicate">
<code class="descname">predicate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.predicate" title="Permalink to this definition">¶</a></dt>
<dd><p>A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.schedule">
<code class="descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Trigger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.get_script">
<code class="descclassname">pulumi_aws.glue.</code><code class="descname">get_script</code><span class="sig-paren">(</span><em>dag_edges=None</em>, <em>dag_nodes=None</em>, <em>language=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.get_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
