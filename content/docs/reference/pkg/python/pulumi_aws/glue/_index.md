---
title: Module glue
---

<div class="section" id="glue">
<h1>glue<a class="headerlink" href="#glue" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.glue"></span><dl class="class">
<dt id="pulumi_aws.glue.AwaitableGetScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">AwaitableGetScriptResult</code><span class="sig-paren">(</span><em class="sig-param">dag_edges=None</em>, <em class="sig-param">dag_nodes=None</em>, <em class="sig-param">language=None</em>, <em class="sig-param">python_script=None</em>, <em class="sig-param">scala_code=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.AwaitableGetScriptResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.glue.CatalogDatabase">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">CatalogDatabase</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Catalog Database Resource. You can refer to the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html">Glue Developer Guide</a> for a full explanation of the Glue Data Catalog functionality</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the database.</p></li>
<li><p><strong>location_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the database (for example, an HDFS path).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of key-value pairs that define parameters and properties of the database.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.location_uri">
<code class="sig-name descname">location_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.location_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the database (for example, an HDFS path).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key-value pairs that define parameters and properties of the database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogDatabase.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CatalogDatabase resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the database.</p></li>
<li><p><strong>location_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the database (for example, an HDFS path).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of key-value pairs that define parameters and properties of the database.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogDatabase.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogDatabase.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">CatalogTable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">partition_keys=None</em>, <em class="sig-param">retention=None</em>, <em class="sig-param">storage_descriptor=None</em>, <em class="sig-param">table_type=None</em>, <em class="sig-param">view_expanded_text=None</em>, <em class="sig-param">view_original_text=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Catalog Table Resource. You can refer to the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html">Glue Developer Guide</a> for a full explanation of the Glue Data Catalog functionality.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the table.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SerDe.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner of the table.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><strong>partition_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p></li>
<li><p><strong>retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention time for this table.</p></li>
<li><p><strong>storage_descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
</p></li>
<li><p><strong>table_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</p></li>
<li><p><strong>view_expanded_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the expanded text of the view; otherwise null.</p></li>
<li><p><strong>view_original_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the original text of the view; otherwise null.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SerDe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Owner of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of initialization parameters for the SerDe, in key-value form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.partition_keys">
<code class="sig-name descname">partition_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.partition_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.retention">
<code class="sig-name descname">retention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.retention" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention time for this table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.storage_descriptor">
<code class="sig-name descname">storage_descriptor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.storage_descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.table_type">
<code class="sig-name descname">table_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.table_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_expanded_text">
<code class="sig-name descname">view_expanded_text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_expanded_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the expanded text of the view; otherwise null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_original_text">
<code class="sig-name descname">view_original_text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_original_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the original text of the view; otherwise null.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">partition_keys=None</em>, <em class="sig-param">retention=None</em>, <em class="sig-param">storage_descriptor=None</em>, <em class="sig-param">table_type=None</em>, <em class="sig-param">view_expanded_text=None</em>, <em class="sig-param">view_original_text=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CatalogTable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the table.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SerDe.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner of the table.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><strong>partition_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p></li>
<li><p><strong>retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention time for this table.</p></li>
<li><p><strong>storage_descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
</p></li>
<li><p><strong>table_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</p></li>
<li><p><strong>view_expanded_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the expanded text of the view; otherwise null.</p></li>
<li><p><strong>view_original_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the table is a view, the original text of the view; otherwise null.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.CatalogTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Classifier</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">grok_classifier=None</em>, <em class="sig-param">json_classifier=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xml_classifier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Classifier resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> It is only valid to create one type of classifier (grok, JSON, or XML). Changing classifier types will recreate the classifier.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>grok_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier that uses grok patterns. Defined below.</p></li>
<li><p><strong>json_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for JSON content. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the classifier.</p></li>
<li><p><strong>xml_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for XML content. Defined below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.grok_classifier">
<code class="sig-name descname">grok_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.grok_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier that uses grok patterns. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.json_classifier">
<code class="sig-name descname">json_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.json_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for JSON content. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the classifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Classifier.xml_classifier">
<code class="sig-name descname">xml_classifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.xml_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for XML content. Defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Classifier.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">grok_classifier=None</em>, <em class="sig-param">json_classifier=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xml_classifier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Classifier resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>grok_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier that uses grok patterns. Defined below.</p></li>
<li><p><strong>json_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for JSON content. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the classifier.</p></li>
<li><p><strong>xml_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for XML content. Defined below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Classifier.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">connection_properties=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">match_criterias=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_connection_requirements=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Connection resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</p></li>
<li><p><strong>connection_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key-value pairs used as parameters for this connection.</p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the connection.</p></li>
<li><p><strong>match_criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of criteria that can be used in selecting this connection.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
<li><p><strong>physical_connection_requirements</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.connection_properties">
<code class="sig-name descname">connection_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key-value pairs used as parameters for this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.connection_type">
<code class="sig-name descname">connection_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.match_criterias">
<code class="sig-name descname">match_criterias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.match_criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of criteria that can be used in selecting this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Connection.physical_connection_requirements">
<code class="sig-name descname">physical_connection_requirements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.physical_connection_requirements" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_id=None</em>, <em class="sig-param">connection_properties=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">match_criterias=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_connection_requirements=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</p></li>
<li><p><strong>connection_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key-value pairs used as parameters for this connection.</p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the connection.</p></li>
<li><p><strong>match_criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of criteria that can be used in selecting this connection.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
<li><p><strong>physical_connection_requirements</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Crawler</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">catalog_targets=None</em>, <em class="sig-param">classifiers=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb_targets=None</em>, <em class="sig-param">jdbc_targets=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">s3_targets=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">schema_change_policy=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">table_prefix=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Crawler. More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">AWS Glue Developer Guide</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>classifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of configuration information.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glue database to be synchronized.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the crawler.</p></li>
<li><p><strong>dynamodb_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested DynamoDB target arguments. See below.</p></li>
<li><p><strong>jdbc_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested JBDC target arguments. See below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the crawler.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</p></li>
<li><p><strong>s3_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List nested Amazon S3 target arguments. See below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</p></li>
<li><p><strong>schema_change_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy for the crawler’s update and deletion behavior.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of Security Configuration to be used by the crawler</p></li>
<li><p><strong>table_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table prefix used for catalog tables that are created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the crawler</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.classifiers">
<code class="sig-name descname">classifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.classifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.configuration">
<code class="sig-name descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string of configuration information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Glue database to be synchronized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the crawler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.dynamodb_targets">
<code class="sig-name descname">dynamodb_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.dynamodb_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested DynamoDB target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.jdbc_targets">
<code class="sig-name descname">jdbc_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.jdbc_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested JBDC target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the crawler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.s3_targets">
<code class="sig-name descname">s3_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.s3_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List nested Amazon S3 target arguments. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.schedule">
<code class="sig-name descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.schema_change_policy">
<code class="sig-name descname">schema_change_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schema_change_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy for the crawler’s update and deletion behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of Security Configuration to be used by the crawler</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Crawler.table_prefix">
<code class="sig-name descname">table_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.table_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The table prefix used for catalog tables that are created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Crawler.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">catalog_targets=None</em>, <em class="sig-param">classifiers=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb_targets=None</em>, <em class="sig-param">jdbc_targets=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">s3_targets=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">schema_change_policy=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">table_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Crawler resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the crawler</p></li>
<li><p><strong>classifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of configuration information.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glue database to be synchronized.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the crawler.</p></li>
<li><p><strong>dynamodb_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested DynamoDB target arguments. See below.</p></li>
<li><p><strong>jdbc_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of nested JBDC target arguments. See below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the crawler.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</p></li>
<li><p><strong>s3_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List nested Amazon S3 target arguments. See below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</p>
</p></li>
<li><p><strong>schema_change_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy for the crawler’s update and deletion behavior.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of Security Configuration to be used by the crawler</p></li>
<li><p><strong>table_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table prefix used for catalog tables that are created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Crawler.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.GetScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">GetScriptResult</code><span class="sig-paren">(</span><em class="sig-param">dag_edges=None</em>, <em class="sig-param">dag_nodes=None</em>, <em class="sig-param">language=None</em>, <em class="sig-param">python_script=None</em>, <em class="sig-param">scala_code=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScript.</p>
<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.python_script">
<code class="sig-name descname">python_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.python_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Python script generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">PYTHON</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.scala_code">
<code class="sig-name descname">scala_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.scala_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scala code generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">SCALA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.GetScriptResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.glue.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_capacity=None</em>, <em class="sig-param">command=None</em>, <em class="sig-param">connections=None</em>, <em class="sig-param">default_arguments=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_property=None</em>, <em class="sig-param">max_capacity=None</em>, <em class="sig-param">max_retries=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Job resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The command of the job. Defined below.</p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of connections used for this job.</p></li>
<li><p><strong>default_arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the job.</p></li>
<li><p><strong>execution_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Execution property of the job. Defined below.</p></li>
<li><p><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times to retry this job if it fails.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code></p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role associated with this job.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Security Configuration to be associated with the job.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The job timeout in minutes. The default is 2880 minutes (48 hours).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Job.allocated_capacity">
<code class="sig-name descname">allocated_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.allocated_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.command">
<code class="sig-name descname">command</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.command" title="Permalink to this definition">¶</a></dt>
<dd><p>The command of the job. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.connections">
<code class="sig-name descname">connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of connections used for this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.default_arguments">
<code class="sig-name descname">default_arguments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.default_arguments" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.execution_property">
<code class="sig-name descname">execution_property</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.execution_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Execution property of the job. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.max_capacity">
<code class="sig-name descname">max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.max_retries">
<code class="sig-name descname">max_retries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times to retry this job if it fails.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role associated with this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Security Configuration to be associated with the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Job.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The job timeout in minutes. The default is 2880 minutes (48 hours).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_capacity=None</em>, <em class="sig-param">command=None</em>, <em class="sig-param">connections=None</em>, <em class="sig-param">default_arguments=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_property=None</em>, <em class="sig-param">max_capacity=None</em>, <em class="sig-param">max_retries=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The command of the job. Defined below.</p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of connections used for this job.</p></li>
<li><p><strong>default_arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the job.</p></li>
<li><p><strong>execution_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Execution property of the job. Defined below.</p></li>
<li><p><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times to retry this job if it fails.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code></p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role associated with this job.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Security Configuration to be associated with the job.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The job timeout in minutes. The default is 2880 minutes (48 hours).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_job.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">SecurityConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encryption_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Security Configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing encryption configuration. Detailed below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the security configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.encryption_configuration">
<code class="sig-name descname">encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing encryption configuration. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the security configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.SecurityConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encryption_configuration=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing encryption configuration. Detailed below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the security configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_security_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Trigger</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicate=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Trigger resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of actions initiated by this trigger when it fires. Defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the new trigger.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the trigger.</p></li>
<li><p><strong>predicate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of actions initiated by this trigger when it fires. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the new trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.predicate">
<code class="sig-name descname">predicate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.predicate" title="Permalink to this definition">¶</a></dt>
<dd><p>A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.schedule">
<code class="sig-name descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glue.Trigger.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Trigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicate=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of actions initiated by this trigger when it fires. Defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the new trigger.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the trigger.</p></li>
<li><p><strong>predicate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glue.Trigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.get_script">
<code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">get_script</code><span class="sig-paren">(</span><em class="sig-param">dag_edges=None</em>, <em class="sig-param">dag_nodes=None</em>, <em class="sig-param">language=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.get_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
