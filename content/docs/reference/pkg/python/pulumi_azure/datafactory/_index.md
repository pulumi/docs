---
title: Module datafactory
---

<div class="section" id="datafactory">
<h1>datafactory<a class="headerlink" href="#datafactory" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.datafactory"></span><dl class="class">
<dt id="pulumi_azure.datafactory.DatasetMysql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetMysql</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a MySQL Dataset inside a Azure Data Factory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset MySQL.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset MySQL. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset MySQL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset MySQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_mysql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_mysql.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description for the Data Factory Dataset MySQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetMysql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetMysql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset MySQL.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset MySQL. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset MySQL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset MySQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_mysql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_mysql.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetMysql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetMysql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetPostgresql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetPostgresql</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a PostgreSQL Dataset inside a Azure Data Factory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset PostgreSQL. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset PostgreSQL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset PostgreSQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_postgresql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_postgresql.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset PostgreSQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description for the Data Factory Dataset PostgreSQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetPostgresql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset PostgreSQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset PostgreSQL. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset PostgreSQL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset PostgreSQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_postgresql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_postgresql.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetPostgresql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetSqlServerTable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a SQL Server Table Dataset inside a Azure Data Factory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset SQL Server Table. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset SQL Server Table.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset SQL Server Table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_sql_server_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_sql_server_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset SQL Server Table. Changing this forces a new resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description for the Data Factory Dataset SQL Server Table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_columns=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetSqlServerTable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Linked Service name in which to associate the Dataset with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Dataset SQL Server Table.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Dataset SQL Server Table. Changing this forces a new resource</p></li>
<li><p><strong>schema_columns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the Data Factory Dataset SQL Server Table.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>schema_columns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description for the Data Factory Dataset SQL Server Table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_sql_server_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_dataset_sql_server_table.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Factory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">Factory</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">github_configuration=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vsts_configuration=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Data Factory (Version 2).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>github_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">github_configuration</span></code> block as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vsts_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vsts_configuration</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>github_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vsts_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.github_configuration">
<code class="sig-name descname">github_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.github_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">github_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Factory.vsts_configuration">
<code class="sig-name descname">vsts_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.vsts_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vsts_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.Factory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">github_configuration=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vsts_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Factory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>github_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">github_configuration</span></code> block as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vsts_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vsts_configuration</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>github_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vsts_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Azure Active Directory Tenant.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.Factory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Factory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceDataLakeStorageGen2</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_principal_id=None</em>, <em class="sig-param">service_principal_key=None</em>, <em class="sig-param">tenant=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Linked Service (connection) between Data Lake Storage Gen2 and Azure Data Factory.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the <code class="docutils literal notranslate"><span class="pre">service_principal_key</span></code> will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service principal id in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>service_principal_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service principal key in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id or name in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint for the Azure Data Lake Storage Gen2 service.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_data_lake_storage_gen2.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_data_lake_storage_gen2.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_id">
<code class="sig-name descname">service_principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service principal id in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_key">
<code class="sig-name descname">service_principal_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The service principal key in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.tenant">
<code class="sig-name descname">tenant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id or name in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for the Azure Data Lake Storage Gen2 service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_principal_id=None</em>, <em class="sig-param">service_principal_key=None</em>, <em class="sig-param">tenant=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedServiceDataLakeStorageGen2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service principal id in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>service_principal_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service principal key in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id or name in which to authenticate against the Azure Data Lake Storage Gen2 account.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint for the Azure Data Lake Storage Gen2 service.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_data_lake_storage_gen2.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_data_lake_storage_gen2.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceMysql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceMysql</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Linked Service (connection) between MySQL and Azure Data Factory.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the connection_string will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_mysql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_mysql.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedServiceMysql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with MySQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service MySQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_mysql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_mysql.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServicePostgresql</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Linked Service (connection) between PostgreSQL and Azure Data Factory.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the connection_string will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with PostgreSQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service PostgreSQL. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_postgresql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_postgresql.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service PostgreSQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedServicePostgresql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with PostgreSQL.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service PostgreSQL.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service PostgreSQL. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_postgresql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_postgresql.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceSqlServer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Linked Service (connection) between a SQL Server and Azure Data Factory.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the client secret will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with the SQL Server.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service SQL Server. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service SQL Server. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_sql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_sql_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service SQL Server. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service SQL Server. Changing this forces a new resource</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_properties=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_runtime_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedServiceSqlServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string in which to authenticate with the SQL Server.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service SQL Server. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service SQL Server.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service SQL Server. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_sql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_linked_service_sql_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Pipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">Pipeline</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">variables=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Pipeline inside a Azure Data Factory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Pipeline.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Pipeline.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Pipeline.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of variables to associate with the Data Factory Pipeline.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_pipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_pipeline.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.annotations">
<code class="sig-name descname">annotations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datafactory.Pipeline.variables">
<code class="sig-name descname">variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of variables to associate with the Data Factory Pipeline.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.Pipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">annotations=None</em>, <em class="sig-param">data_factory_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">variables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Pipeline.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Pipeline.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Pipeline.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of variables to associate with the Data Factory Pipeline.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_pipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_pipeline.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datafactory.Pipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Pipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
