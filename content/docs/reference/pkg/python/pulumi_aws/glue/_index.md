---
title: Module glue
title_tag: Module glue | Package pulumi_aws | Python SDK
linktitle: glue
notitle: true
---

<div class="section" id="glue">
<h1>glue<a class="headerlink" href="#glue" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.glue"></span><dl class="py class">
<dt id="pulumi_aws.glue.AwaitableGetScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">AwaitableGetScriptResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dag_edges</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dag_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">language</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">python_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scala_code</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.AwaitableGetScriptResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.glue.CatalogDatabase">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">CatalogDatabase</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.location_uri">
<code class="sig-name descname">location_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.location_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the database (for example, an HDFS path).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogDatabase.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key-value pairs that define parameters and properties of the database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.CatalogDatabase.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.CatalogDatabase.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogDatabase.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">CatalogTable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_expanded_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_original_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>partition_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The datatype of data in the Column.</p></li>
</ul>
<p>The <strong>storage_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of reducer grouping columns, clustering columns, and bucketing columns in the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the Columns in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The datatype of data in the Column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the data in the table is compressed, or False if not.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be specified if the table contains any dimension columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serDeInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Serialization/deserialization (SerDe) information.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serializationLibrary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about values that appear very frequently in a column (skewed values).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of names of columns that contain skewed values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValueLocationMaps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of values that appear so frequently as to be considered skewed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A mapping of skewed values to the columns that contain them.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Order objects specifying the sort order of each bucket in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storedAsSubDirectories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the table data is stored in subdirectories, or False if not.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SerDe.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.owner">
<code class="sig-name descname">owner</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Owner of the table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of initialization parameters for the SerDe, in key-value form.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.partition_keys">
<code class="sig-name descname">partition_keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.partition_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The datatype of data in the Column.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.retention">
<code class="sig-name descname">retention</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.retention" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention time for this table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.storage_descriptor">
<code class="sig-name descname">storage_descriptor</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.storage_descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage descriptor object containing information about the physical storage of this table. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor">Glue Developer Guide</a> for a full explanation of this object.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of reducer grouping columns, clustering columns, and bucketing columns in the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the Columns in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The datatype of data in the Column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressed</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - True if the data in the table is compressed, or False if not.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be specified if the table contains any dimension columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serDeInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Serialization/deserialization (SerDe) information.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serializationLibrary</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about values that appear very frequently in a column (skewed values).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of names of columns that contain skewed values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValueLocationMaps</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of values that appear so frequently as to be considered skewed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A mapping of skewed values to the columns that contain them.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Order objects specifying the sort order of each bucket in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storedAsSubDirectories</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - True if the table data is stored in subdirectories, or False if not.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.table_type">
<code class="sig-name descname">table_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.table_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_expanded_text">
<code class="sig-name descname">view_expanded_text</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_expanded_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the expanded text of the view; otherwise null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.CatalogTable.view_original_text">
<code class="sig-name descname">view_original_text</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.view_original_text" title="Permalink to this definition">¶</a></dt>
<dd><p>If the table is a view, the original text of the view; otherwise null.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.CatalogTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_expanded_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_original_text</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.get" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>partition_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The datatype of data in the Column.</p></li>
</ul>
<p>The <strong>storage_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of reducer grouping columns, clustering columns, and bucketing columns in the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the Columns in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Free-form text comment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The datatype of data in the Column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the data in the table is compressed, or False if not.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be specified if the table contains any dimension columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serDeInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Serialization/deserialization (SerDe) information.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the SerDe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of initialization parameters for the SerDe, in key-value form.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serializationLibrary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about values that appear very frequently in a column (skewed values).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of names of columns that contain skewed values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValueLocationMaps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of values that appear so frequently as to be considered skewed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skewedColumnValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A mapping of skewed values to the columns that contain them.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Order objects specifying the sort order of each bucket in the table.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storedAsSubDirectories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the table data is stored in subdirectories, or False if not.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.CatalogTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.CatalogTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.CatalogTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Classifier</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csv_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grok_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">xml_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Classifier resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> It is only valid to create one type of classifier (csv, grok, JSON, or XML). Changing classifier types will recreate the classifier.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>csv_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for Csv content. Defined below.</p></li>
<li><p><strong>grok_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier that uses grok patterns. Defined below.</p></li>
<li><p><strong>json_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for JSON content. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the classifier.</p></li>
<li><p><strong>xml_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for XML content. Defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>csv_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowSingleColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the processing of files that contain only one column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">containsHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether the CSV file contains a header. This can be one of “ABSENT”, “PRESENT”, or “UNKNOWN”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The delimiter used in the Csv to separate columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableValueTrimming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to trim column values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of strings representing column names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quoteSymbol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.</p></li>
</ul>
<p>The <strong>grok_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom grok patterns used by this classifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grokPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The grok pattern used by this classifier.</p></li>
</ul>
<p>The <strong>json_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code> string defining the JSON data for the classifier to classify. AWS Glue supports a subset of <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code>, as described in <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json">Writing JsonPath Custom Classifiers</a>.</p></li>
</ul>
<p>The <strong>xml_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowTag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by <code class="docutils literal notranslate"><span class="pre">/&gt;</span></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;&gt;&lt;/row&gt;</span></code> is okay, but <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;</span> <span class="pre">/&gt;</span></code> is not).</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Classifier.csv_classifier">
<code class="sig-name descname">csv_classifier</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.csv_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for Csv content. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowSingleColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables the processing of files that contain only one column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">containsHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates whether the CSV file contains a header. This can be one of “ABSENT”, “PRESENT”, or “UNKNOWN”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The delimiter used in the Csv to separate columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableValueTrimming</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether to trim column values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of strings representing column names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quoteSymbol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Classifier.grok_classifier">
<code class="sig-name descname">grok_classifier</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.grok_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier that uses grok patterns. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom grok patterns used by this classifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grokPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The grok pattern used by this classifier.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Classifier.json_classifier">
<code class="sig-name descname">json_classifier</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.json_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for JSON content. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code> string defining the JSON data for the classifier to classify. AWS Glue supports a subset of <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code>, as described in <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json">Writing JsonPath Custom Classifiers</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Classifier.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the classifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Classifier.xml_classifier">
<code class="sig-name descname">xml_classifier</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Classifier.xml_classifier" title="Permalink to this definition">¶</a></dt>
<dd><p>A classifier for XML content. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowTag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by <code class="docutils literal notranslate"><span class="pre">/&gt;</span></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;&gt;&lt;/row&gt;</span></code> is okay, but <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;</span> <span class="pre">/&gt;</span></code> is not).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Classifier.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csv_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grok_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_classifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">xml_classifier</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Classifier resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>csv_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for Csv content. Defined below.</p></li>
<li><p><strong>grok_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier that uses grok patterns. Defined below.</p></li>
<li><p><strong>json_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for JSON content. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the classifier.</p></li>
<li><p><strong>xml_classifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A classifier for XML content. Defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>csv_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowSingleColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the processing of files that contain only one column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">containsHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether the CSV file contains a header. This can be one of “ABSENT”, “PRESENT”, or “UNKNOWN”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The delimiter used in the Csv to separate columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableValueTrimming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to trim column values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of strings representing column names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quoteSymbol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.</p></li>
</ul>
<p>The <strong>grok_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom grok patterns used by this classifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grokPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The grok pattern used by this classifier.</p></li>
</ul>
<p>The <strong>json_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code> string defining the JSON data for the classifier to classify. AWS Glue supports a subset of <code class="docutils literal notranslate"><span class="pre">JsonPath</span></code>, as described in <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json">Writing JsonPath Custom Classifiers</a>.</p></li>
</ul>
<p>The <strong>xml_classifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">classification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An identifier of the data format that the classifier matches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowTag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by <code class="docutils literal notranslate"><span class="pre">/&gt;</span></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;&gt;&lt;/row&gt;</span></code> is okay, but <code class="docutils literal notranslate"><span class="pre">&lt;row</span> <span class="pre">item_a=&quot;A&quot;</span> <span class="pre">item_b=&quot;B&quot;</span> <span class="pre">/&gt;</span></code> is not).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Classifier.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Classifier.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Classifier.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_connection_requirements</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>physical_connection_requirements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The availability zone of the connection. This field is redundant and implied by <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>, but is currently an api requirement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIdLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security group ID list used by the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet ID used by the connection.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.catalog_id">
<code class="sig-name descname">catalog_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.catalog_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.connection_properties">
<code class="sig-name descname">connection_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key-value pairs used as parameters for this connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.connection_type">
<code class="sig-name descname">connection_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the connection. Defaults to <code class="docutils literal notranslate"><span class="pre">JBDC</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.match_criterias">
<code class="sig-name descname">match_criterias</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.match_criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of criteria that can be used in selecting this connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Connection.physical_connection_requirements">
<code class="sig-name descname">physical_connection_requirements</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Connection.physical_connection_requirements" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The availability zone of the connection. This field is redundant and implied by <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>, but is currently an api requirement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIdLists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The security group ID list used by the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subnet ID used by the connection.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_connection_requirements</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.get" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>physical_connection_requirements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The availability zone of the connection. This field is redundant and implied by <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>, but is currently an api requirement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIdLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security group ID list used by the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet ID used by the connection.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Crawler</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classifiers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamodb_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jdbc_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_change_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glue Crawler. More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">AWS Glue Developer Guide</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>classifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of configuration information.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Glue database where results are written.</p></li>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>catalog_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Glue database to be synchronized.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of catalog tables to be synchronized.</p></li>
</ul>
<p>The <strong>dynamodb_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
<p>The <strong>jdbc_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the connection to use to connect to the JDBC target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the JDBC target.</p></li>
</ul>
<p>The <strong>s3_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
<p>The <strong>schema_change_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The deletion behavior when the crawler finds a deleted object. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE_FROM_DATABASE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The update behavior when the crawler finds a changed schema. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code> or <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the crawler</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.classifiers">
<code class="sig-name descname">classifiers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.classifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.configuration">
<code class="sig-name descname">configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string of configuration information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Glue database where results are written.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the crawler.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.dynamodb_targets">
<code class="sig-name descname">dynamodb_targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.dynamodb_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested DynamoDB target arguments. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.jdbc_targets">
<code class="sig-name descname">jdbc_targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.jdbc_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of nested JBDC target arguments. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the connection to use to connect to the JDBC target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of the JDBC target.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the crawler.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.s3_targets">
<code class="sig-name descname">s3_targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.s3_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List nested Amazon S3 target arguments. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.schedule">
<code class="sig-name descname">schedule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code class="docutils literal notranslate"><span class="pre">cron(15</span> <span class="pre">12</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.schema_change_policy">
<code class="sig-name descname">schema_change_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.schema_change_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy for the crawler’s update and deletion behavior.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The deletion behavior when the crawler finds a deleted object. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE_FROM_DATABASE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The update behavior when the crawler finds a changed schema. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code> or <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of Security Configuration to be used by the crawler</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.table_prefix">
<code class="sig-name descname">table_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.table_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The table prefix used for catalog tables that are created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Crawler.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Crawler.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Crawler.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classifiers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamodb_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jdbc_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_change_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Glue database where results are written.</p></li>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>catalog_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Glue database to be synchronized.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of catalog tables to be synchronized.</p></li>
</ul>
<p>The <strong>dynamodb_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
<p>The <strong>jdbc_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the connection to use to connect to the JDBC target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the JDBC target.</p></li>
</ul>
<p>The <strong>s3_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of glob patterns used to exclude from the crawl.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the DynamoDB table to crawl.</p></li>
</ul>
<p>The <strong>schema_change_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The deletion behavior when the crawler finds a deleted object. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE_FROM_DATABASE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEPRECATE_IN_DATABASE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateBehavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The update behavior when the crawler finds a changed schema. Valid values: <code class="docutils literal notranslate"><span class="pre">LOG</span></code> or <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">UPDATE_IN_DATABASE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Crawler.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Crawler.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Crawler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.GetScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">GetScriptResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dag_edges</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dag_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">language</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">python_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scala_code</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScript.</p>
<dl class="py attribute">
<dt id="pulumi_aws.glue.GetScriptResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.GetScriptResult.python_script">
<code class="sig-name descname">python_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.python_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Python script generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">PYTHON</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.GetScriptResult.scala_code">
<code class="sig-name descname">scala_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.GetScriptResult.scala_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scala code generated from the DAG when the <code class="docutils literal notranslate"><span class="pre">language</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">SCALA</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.glue.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_arguments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_property</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">glue_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_property</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_workers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Job resource.</p>
<blockquote>
<div><p>Glue functionality, such as monitoring and logging of jobs, is typically managed with the <code class="docutils literal notranslate"><span class="pre">default_arguments</span></code> argument. See the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the Glue developer guide for additional information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The command of the job. Defined below.</p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of connections used for this job.</p></li>
<li><p><strong>default_arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the job.</p></li>
<li><p><strong>execution_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Execution property of the job. Defined below.</p></li>
<li><p><strong>glue_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of glue to use, for example “1.0”. For information about available versions, see the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">AWS Glue Release Notes</a>.</p></li>
<li><p><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. <code class="docutils literal notranslate"><span class="pre">Required</span></code> when <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is set, accept either <code class="docutils literal notranslate"><span class="pre">0.0625</span></code> or <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times to retry this job if it fails.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you assign to this job. It must be unique in your account.</p></li>
<li><p><strong>notification_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Notification property of the job. Defined below.</p></li>
<li><p><strong>number_of_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers of a defined workerType that are allocated when a job runs.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role associated with this job.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Security Configuration to be associated with the job.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The job timeout in minutes. The default is 2880 minutes (48 hours).</p></li>
<li><p><strong>worker_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>command</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code>. Use <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> for Python Shell Job Type, <code class="docutils literal notranslate"><span class="pre">max_capacity</span></code> needs to be set if <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is chosen.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Python version being used to execute a Python shell job. Allowed values are 2 or 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the S3 path to a script that executes a job.</p></li>
</ul>
<p>The <strong>execution_property</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRuns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of concurrent runs allowed for a job. The default is 1.</p></li>
</ul>
<p>The <strong>notification_property</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">notifyDelayAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After a job run starts, the number of minutes to wait before sending a job run delay notification.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.allocated_capacity">
<code class="sig-name descname">allocated_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.allocated_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Glue Job</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.command">
<code class="sig-name descname">command</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.command" title="Permalink to this definition">¶</a></dt>
<dd><p>The command of the job. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code>. Use <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> for Python Shell Job Type, <code class="docutils literal notranslate"><span class="pre">max_capacity</span></code> needs to be set if <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is chosen.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Python version being used to execute a Python shell job. Allowed values are 2 or 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the S3 path to a script that executes a job.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.connections">
<code class="sig-name descname">connections</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of connections used for this job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.default_arguments">
<code class="sig-name descname">default_arguments</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.default_arguments" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.execution_property">
<code class="sig-name descname">execution_property</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.execution_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Execution property of the job. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRuns</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of concurrent runs allowed for a job. The default is 1.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.glue_version">
<code class="sig-name descname">glue_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.glue_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of glue to use, for example “1.0”. For information about available versions, see the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">AWS Glue Release Notes</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.max_capacity">
<code class="sig-name descname">max_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. <code class="docutils literal notranslate"><span class="pre">Required</span></code> when <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is set, accept either <code class="docutils literal notranslate"><span class="pre">0.0625</span></code> or <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.max_retries">
<code class="sig-name descname">max_retries</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.max_retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times to retry this job if it fails.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you assign to this job. It must be unique in your account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.notification_property">
<code class="sig-name descname">notification_property</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.notification_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Notification property of the job. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">notifyDelayAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - After a job run starts, the number of minutes to wait before sending a job run delay notification.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.number_of_workers">
<code class="sig-name descname">number_of_workers</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.number_of_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of workers of a defined workerType that are allocated when a job runs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role associated with this job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Security Configuration to be associated with the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The job timeout in minutes. The default is 2880 minutes (48 hours).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Job.worker_type">
<code class="sig-name descname">worker_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Job.worker_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_arguments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_property</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">glue_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_property</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_workers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED</strong> (Optional) The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of Glue Job</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The command of the job. Defined below.</p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of connections used for this job.</p></li>
<li><p><strong>default_arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling AWS Glue APIs in Python</a> topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the <a class="reference external" href="http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html">Special Parameters Used by AWS Glue</a> topic in the developer guide.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the job.</p></li>
<li><p><strong>execution_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Execution property of the job. Defined below.</p></li>
<li><p><strong>glue_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The version of glue to use, for example “1.0”. For information about available versions, see the <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">AWS Glue Release Notes</a>.</p>
</p></li>
<li><p><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. <code class="docutils literal notranslate"><span class="pre">Required</span></code> when <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is set, accept either <code class="docutils literal notranslate"><span class="pre">0.0625</span></code> or <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times to retry this job if it fails.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you assign to this job. It must be unique in your account.</p></li>
<li><p><strong>notification_property</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Notification property of the job. Defined below.</p></li>
<li><p><strong>number_of_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers of a defined workerType that are allocated when a job runs.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role associated with this job.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Security Configuration to be associated with the job.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The job timeout in minutes. The default is 2880 minutes (48 hours).</p></li>
<li><p><strong>worker_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>command</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job command. Defaults to <code class="docutils literal notranslate"><span class="pre">glueetl</span></code>. Use <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> for Python Shell Job Type, <code class="docutils literal notranslate"><span class="pre">max_capacity</span></code> needs to be set if <code class="docutils literal notranslate"><span class="pre">pythonshell</span></code> is chosen.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Python version being used to execute a Python shell job. Allowed values are 2 or 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the S3 path to a script that executes a job.</p></li>
</ul>
<p>The <strong>execution_property</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRuns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of concurrent runs allowed for a job. The default is 1.</p></li>
</ul>
<p>The <strong>notification_property</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">notifyDelayAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After a job run starts, the number of minutes to wait before sending a job run delay notification.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">SecurityConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for CloudWatch data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for job bookmarks data. Valid values: <code class="docutils literal notranslate"><span class="pre">CSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Encryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">s3_encryption</span></code> block as described below, which contains encryption configuration for S3 data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3EncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for S3 data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-S3</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.encryption_configuration">
<code class="sig-name descname">encryption_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing encryption configuration. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Encryption mode to use for CloudWatch data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Encryption mode to use for job bookmarks data. Valid values: <code class="docutils literal notranslate"><span class="pre">CSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Encryption</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">s3_encryption</span></code> block as described below, which contains encryption configuration for S3 data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3EncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Encryption mode to use for S3 data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-S3</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.SecurityConfiguration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the security configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.SecurityConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.get" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for CloudWatch data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jobBookmarksEncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for job bookmarks data. Valid values: <code class="docutils literal notranslate"><span class="pre">CSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Encryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">s3_encryption</span></code> block as described below, which contains encryption configuration for S3 data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3EncryptionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption mode to use for S3 data. Valid values: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-KMS</span></code>, <code class="docutils literal notranslate"><span class="pre">SSE-S3</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.SecurityConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Trigger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p></li>
<li><p><strong>workflow_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (<code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code> type) and can contain multiple additional <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code> triggers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the crawler to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a job to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The job run timeout in minutes. It overrides the timeout value of the job.</p></li>
</ul>
<p>The <strong>predicate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the conditions that determine when the trigger will fire. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The condition crawl state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">RUNNING</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCELLED</span></code>, and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">state</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the crawler to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawl_state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logicalOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A logical operator. Defaults to <code class="docutils literal notranslate"><span class="pre">EQUALS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The condition job state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">STOPPED</span></code>, <code class="docutils literal notranslate"><span class="pre">TIMEOUT</span></code> and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">job_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_state</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logical</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to handle multiple conditions. Defaults to <code class="docutils literal notranslate"><span class="pre">AND</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">AND</span></code> or <code class="docutils literal notranslate"><span class="pre">ANY</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.actions">
<code class="sig-name descname">actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of actions initiated by this trigger when it fires. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the crawler to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a job to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The job run timeout in minutes. It overrides the timeout value of the job.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Glue Trigger</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the new trigger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the trigger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.predicate">
<code class="sig-name descname">predicate</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.predicate" title="Permalink to this definition">¶</a></dt>
<dd><p>A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the conditions that determine when the trigger will fire. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The condition crawl state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">RUNNING</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCELLED</span></code>, and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">state</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the crawler to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawl_state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logicalOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A logical operator. Defaults to <code class="docutils literal notranslate"><span class="pre">EQUALS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The condition job state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">STOPPED</span></code>, <code class="docutils literal notranslate"><span class="pre">TIMEOUT</span></code> and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">job_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_state</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logical</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How to handle multiple conditions. Defaults to <code class="docutils literal notranslate"><span class="pre">AND</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">AND</span></code> or <code class="docutils literal notranslate"><span class="pre">ANY</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.schedule">
<code class="sig-name descname">schedule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Trigger.workflow_name">
<code class="sig-name descname">workflow_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Trigger.workflow_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (<code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code> type) and can contain multiple additional <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code> triggers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Trigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of actions initiated by this trigger when it fires. Defined below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of Glue Trigger</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the new trigger.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Start the trigger. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Not valid to disable for <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the trigger.</p></li>
<li><p><strong>predicate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A predicate to specify when the new trigger should fire. Required when trigger type is <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>. Defined below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A cron expression used to specify the schedule. <a class="reference external" href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a></p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of trigger. Valid values are <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code>.</p></li>
<li><p><strong>workflow_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (<code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">SCHEDULED</span></code> type) and can contain multiple additional <code class="docutils literal notranslate"><span class="pre">CONDITIONAL</span></code> triggers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the crawler to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a job to be executed. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The job run timeout in minutes. It overrides the timeout value of the job.</p></li>
</ul>
<p>The <strong>predicate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the conditions that determine when the trigger will fire. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The condition crawl state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">RUNNING</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCELLED</span></code>, and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">state</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crawlerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the crawler to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">crawl_state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">job_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job to watch. If this is specified, <code class="docutils literal notranslate"><span class="pre">state</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logicalOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A logical operator. Defaults to <code class="docutils literal notranslate"><span class="pre">EQUALS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The condition job state. Currently, the values supported are <code class="docutils literal notranslate"><span class="pre">SUCCEEDED</span></code>, <code class="docutils literal notranslate"><span class="pre">STOPPED</span></code>, <code class="docutils literal notranslate"><span class="pre">TIMEOUT</span></code> and <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. If this is specified, <code class="docutils literal notranslate"><span class="pre">job_name</span></code> must also be specified. Conflicts with <code class="docutils literal notranslate"><span class="pre">crawler_state</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logical</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to handle multiple conditions. Defaults to <code class="docutils literal notranslate"><span class="pre">AND</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">AND</span></code> or <code class="docutils literal notranslate"><span class="pre">ANY</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Trigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Trigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Workflow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">Workflow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_run_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Workflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glue Workflow resource.
The workflow graph (DAG) can be build using the <code class="docutils literal notranslate"><span class="pre">glue.Trigger</span></code> resource. 
See the example below for creating a graph with four nodes (two triggers and two jobs).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_run_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the workflow.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you assign to this workflow.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.glue.Workflow.default_run_properties">
<code class="sig-name descname">default_run_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Workflow.default_run_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Workflow.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Workflow.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glue.Workflow.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glue.Workflow.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you assign to this workflow.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Workflow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_run_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Workflow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workflow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_run_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the workflow.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you assign to this workflow.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glue.Workflow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Workflow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.Workflow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.Workflow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glue.get_script">
<code class="sig-prename descclassname">pulumi_aws.glue.</code><code class="sig-name descname">get_script</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dag_edges</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dag_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">language</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glue.get_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dag_edges</strong> (<em>list</em>) – A list of the edges in the DAG. Defined below.</p></li>
<li><p><strong>dag_nodes</strong> (<em>list</em>) – A list of the nodes in the DAG. Defined below.</p></li>
<li><p><strong>language</strong> (<em>str</em>) – The programming language of the resulting code from the DAG. Defaults to <code class="docutils literal notranslate"><span class="pre">PYTHON</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">PYTHON</span></code> and <code class="docutils literal notranslate"><span class="pre">SCALA</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dag_edges</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the node at which the edge starts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the node at which the edge ends.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The target of the edge.</p></li>
</ul>
<p>The <strong>dag_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Nested configuration an argument or property of a node. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the argument or property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">param</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean if the value is used as a parameter. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the argument or property.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A node identifier that is unique within the node’s graph.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lineNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The line number of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of node this is.</p></li>
</ul>
</dd></dl>

</div>
