---
title: Module datafactory
title_tag: Module datafactory | Package pulumi_azure | Python SDK
linktitle: datafactory
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="datafactory">
<h1>datafactory<a class="headerlink" href="#datafactory" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.datafactory"></span><dl class="py class">
<dt id="pulumi_azure.datafactory.AwaitableGetFactoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">AwaitableGetFactoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">github_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsts_configurations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.AwaitableGetFactoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datafactory.DatasetMysql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetMysql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MySQL Dataset inside a Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_mysql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceMysql</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceMysql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Server=test;Port=3306;Database=test;User=test;SSLMode=1;UseSystemTrustStore=0;Password=test&quot;</span><span class="p">)</span>
<span class="n">example_dataset_mysql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">DatasetMysql</span><span class="p">(</span><span class="s2">&quot;exampleDatasetMysql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">linked_service_name</span><span class="o">=</span><span class="n">example_linked_service_mysql</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetMysql.table_name">
<code class="sig-name descname">table_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset MySQL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetMysql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetMysql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetMysql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetMysql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetPostgresql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetPostgresql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Dataset inside a Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_postgresql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServicePostgresql</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServicePostgresql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Host=example;Port=5432;Database=example;UID=example;EncryptionMethod=0;Password=example&quot;</span><span class="p">)</span>
<span class="n">example_dataset_postgresql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">DatasetPostgresql</span><span class="p">(</span><span class="s2">&quot;exampleDatasetPostgresql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">linked_service_name</span><span class="o">=</span><span class="n">example_linked_service_postgresql</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset PostgreSQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.table_name">
<code class="sig-name descname">table_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset PostgreSQL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetPostgresql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetPostgresql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetPostgresql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">DatasetSqlServerTable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SQL Server Table Dataset inside a Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceSqlServer</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Integrated Security=False;Data Source=test;Initial Catalog=test;User ID=test;Password=test&quot;</span><span class="p">)</span>
<span class="n">example_dataset_sql_server_table</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">DatasetSqlServerTable</span><span class="p">(</span><span class="s2">&quot;exampleDatasetSqlServerTable&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">linked_service_name</span><span class="o">=</span><span class="n">example_linked_service_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Linked Service name in which to associate the Dataset with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Dataset SQL Server Table. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Dataset SQL Server Table. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.schema_columns">
<code class="sig-name descname">schema_columns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.schema_columns" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">schema_column</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.table_name">
<code class="sig-name descname">table_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the Data Factory Dataset SQL Server Table.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_columns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the column. Valid values are <code class="docutils literal notranslate"><span class="pre">Byte</span></code>, <code class="docutils literal notranslate"><span class="pre">Byte[]</span></code>, <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Date</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>,<code class="docutils literal notranslate"><span class="pre">DateTimeOffset</span></code>, <code class="docutils literal notranslate"><span class="pre">Decimal</span></code>, <code class="docutils literal notranslate"><span class="pre">Double</span></code>, <code class="docutils literal notranslate"><span class="pre">Guid</span></code>, <code class="docutils literal notranslate"><span class="pre">Int16</span></code>, <code class="docutils literal notranslate"><span class="pre">Int32</span></code>, <code class="docutils literal notranslate"><span class="pre">Int64</span></code>, <code class="docutils literal notranslate"><span class="pre">Single</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeSpan</span></code>. Please note these values are case sensitive.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.DatasetSqlServerTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.DatasetSqlServerTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Factory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">Factory</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">github_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsts_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Data Factory (Version 2).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the GitHub account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the GitHub Enterprise host name. For example: <a class="reference external" href="https://github.mydomain.com">https://github.mydomain.com</a>. Use <a class="reference external" href="https://github.com">https://github.com</a> for open source repositories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Data Factory. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>vsts_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the VSTS account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the VSTS project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.github_configuration">
<code class="sig-name descname">github_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.github_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">github_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the GitHub account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the GitHub Enterprise host name. For example: <a class="reference external" href="https://github.mydomain.com">https://github.mydomain.com</a>. Use <a class="reference external" href="https://github.com">https://github.com</a> for open source repositories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.identity">
<code class="sig-name descname">identity</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the Data Factory. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Factory.vsts_configuration">
<code class="sig-name descname">vsts_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Factory.vsts_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vsts_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the VSTS account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the VSTS project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.Factory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">github_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsts_configuration</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the GitHub account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the GitHub Enterprise host name. For example: <a class="reference external" href="https://github.mydomain.com">https://github.mydomain.com</a>. Use <a class="reference external" href="https://github.com">https://github.com</a> for open source repositories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Principal (Client) in Azure Active Directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Data Factory. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>vsts_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the VSTS account name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the branch of the repository to get code from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the VSTS project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the root folder within the repository. Set to <code class="docutils literal notranslate"><span class="pre">/</span></code> for the top level.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Tenant ID associated with the VSTS account.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.Factory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Factory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Factory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.GetFactoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">GetFactoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">github_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsts_configurations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFactory.</p>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.github_configurations">
<code class="sig-name descname">github_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.github_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">github_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.identities">
<code class="sig-name descname">identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.identities" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the resource exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.GetFactoryResult.vsts_configurations">
<code class="sig-name descname">vsts_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.GetFactoryResult.vsts_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vsts_configuration</span></code> block as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">IntegrationRuntimeManaged</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_parallel_executions_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_integration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Data Factory Managed Integration Runtime.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_integration_runtime_managed</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">IntegrationRuntimeManaged</span><span class="p">(</span><span class="s2">&quot;exampleIntegrationRuntimeManaged&quot;</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">node_size</span><span class="o">=</span><span class="s2">&quot;Standard_D8_v3&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">catalog_info</span></code> block as defined below.</p></li>
<li><p><strong>custom_setup_script</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_setup_script</span></code> block as defined below.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Managed Integration Runtime edition. Valid values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the license that is used. Valid values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrize</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_parallel_executions_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the maximum parallel executions per node. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Max is <code class="docutils literal notranslate"><span class="pre">16</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>node_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the nodes on which the Managed Integration Runtime runs. Valid values are: <code class="docutils literal notranslate"><span class="pre">Standard_D2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D1_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D2_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D3_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_A4_v2</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_A8_v2</span></code></p></li>
<li><p><strong>number_of_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes for the Managed Integration Runtime. Max is <code class="docutils literal notranslate"><span class="pre">10</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_integration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vnet_integration</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>catalog_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Administrator login name for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">administratorPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Administrator login password for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricing_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Pricing tier for the database that will be created for the SSIS catalog. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code> and <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The endpoint of an Azure SQL Server that will be used to host the SSIS catalog.</p></li>
</ul>
<p>The <strong>custom_setup_script</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The blob endpoint for the container which contains a custom setup script that will be run on every node on startup. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A container SAS token that gives access to the files. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
</ul>
<p>The <strong>vnet_integration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the subnet to which the nodes of the Managed Integration Runtime will be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the virtual network to which the nodes of the Managed Integration Runtime will be added.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.catalog_info">
<code class="sig-name descname">catalog_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.catalog_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">catalog_info</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Administrator login name for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">administratorPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Administrator login password for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricing_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Pricing tier for the database that will be created for the SSIS catalog. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code> and <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The endpoint of an Azure SQL Server that will be used to host the SSIS catalog.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.custom_setup_script">
<code class="sig-name descname">custom_setup_script</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.custom_setup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_setup_script</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The blob endpoint for the container which contains a custom setup script that will be run on every node on startup. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A container SAS token that gives access to the files. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.edition">
<code class="sig-name descname">edition</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The Managed Integration Runtime edition. Valid values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.license_type">
<code class="sig-name descname">license_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the license that is used. Valid values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrize</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.max_parallel_executions_per_node">
<code class="sig-name descname">max_parallel_executions_per_node</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.max_parallel_executions_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the maximum parallel executions per node. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Max is <code class="docutils literal notranslate"><span class="pre">16</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.node_size">
<code class="sig-name descname">node_size</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.node_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the nodes on which the Managed Integration Runtime runs. Valid values are: <code class="docutils literal notranslate"><span class="pre">Standard_D2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D1_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D2_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D3_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_A4_v2</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_A8_v2</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.number_of_nodes">
<code class="sig-name descname">number_of_nodes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.number_of_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of nodes for the Managed Integration Runtime. Max is <code class="docutils literal notranslate"><span class="pre">10</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.vnet_integration">
<code class="sig-name descname">vnet_integration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.vnet_integration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vnet_integration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the subnet to which the nodes of the Managed Integration Runtime will be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the virtual network to which the nodes of the Managed Integration Runtime will be added.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catalog_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_parallel_executions_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_integration</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationRuntimeManaged resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>catalog_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">catalog_info</span></code> block as defined below.</p></li>
<li><p><strong>custom_setup_script</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_setup_script</span></code> block as defined below.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Managed Integration Runtime edition. Valid values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the license that is used. Valid values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrize</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_parallel_executions_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the maximum parallel executions per node. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Max is <code class="docutils literal notranslate"><span class="pre">16</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>node_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the nodes on which the Managed Integration Runtime runs. Valid values are: <code class="docutils literal notranslate"><span class="pre">Standard_D2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E2_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E4_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E8_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E16_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E32_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_E64_v3</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D1_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D2_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D3_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_D4_v2</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_A4_v2</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_A8_v2</span></code></p></li>
<li><p><strong>number_of_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes for the Managed Integration Runtime. Max is <code class="docutils literal notranslate"><span class="pre">10</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_integration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vnet_integration</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>catalog_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Administrator login name for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">administratorPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Administrator login password for the SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricing_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Pricing tier for the database that will be created for the SSIS catalog. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code> and <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The endpoint of an Azure SQL Server that will be used to host the SSIS catalog.</p></li>
</ul>
<p>The <strong>custom_setup_script</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The blob endpoint for the container which contains a custom setup script that will be run on every node on startup. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A container SAS token that gives access to the files. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup">https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup</a> for more information.</p></li>
</ul>
<p>The <strong>vnet_integration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the subnet to which the nodes of the Managed Integration Runtime will be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the virtual network to which the nodes of the Managed Integration Runtime will be added.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.IntegrationRuntimeManaged.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeManaged.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">IntegrationRuntimeSelfHosted</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rbac_authorizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Data Factory Self-host Integration Runtime.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;eastus&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_integration_runtime_self_hosted</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">IntegrationRuntimeSelfHosted</span><span class="p">(</span><span class="s2">&quot;exampleIntegrationRuntimeSelfHosted&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Changing this forces a new Data Factory to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Integration runtime description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.</p></li>
<li><p><strong>rbac_authorizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rbac_authorization</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rbac_authorizations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource identifier of the integration runtime to be shared. Changing this forces a new Data Factory to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.auth_key1">
<code class="sig-name descname">auth_key1</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.auth_key1" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary integration runtime authentication key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.auth_key2">
<code class="sig-name descname">auth_key2</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.auth_key2" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary integration runtime authentication key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Changing this forces a new Data Factory to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Integration runtime description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.rbac_authorizations">
<code class="sig-name descname">rbac_authorizations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.rbac_authorizations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rbac_authorization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource identifier of the integration runtime to be shared. Changing this forces a new Data Factory to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_key1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_key2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rbac_authorizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationRuntimeSelfHosted resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_key1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary integration runtime authentication key.</p></li>
<li><p><strong>auth_key2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary integration runtime authentication key.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Changing this forces a new Data Factory to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Integration runtime description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.</p></li>
<li><p><strong>rbac_authorizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rbac_authorization</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rbac_authorizations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource identifier of the integration runtime to be shared. Changing this forces a new Data Factory to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.IntegrationRuntimeSelfHosted.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceDataLakeStorageGen2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linked Service (connection) between Data Lake Storage Gen2 and Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">current</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">example_linked_service_data_lake_storage_gen2</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceDataLakeStorageGen2</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceDataLakeStorageGen2&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">service_principal_id</span><span class="o">=</span><span class="n">current</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span>
    <span class="n">service_principal_key</span><span class="o">=</span><span class="s2">&quot;exampleKey&quot;</span><span class="p">,</span>
    <span class="n">tenant</span><span class="o">=</span><span class="s2">&quot;11111111-1111-1111-1111-111111111111&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://datalakestoragegen2&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_id">
<code class="sig-name descname">service_principal_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service principal id in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_key">
<code class="sig-name descname">service_principal_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.service_principal_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The service principal key in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.tenant">
<code class="sig-name descname">tenant</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id or name in which to authenticate against the Azure Data Lake Storage Gen2 account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for the Azure Data Lake Storage Gen2 service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceDataLakeStorageGen2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceKeyVault</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linked Service (connection) between Key Vault and Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;eastus&quot;</span><span class="p">)</span>
<span class="n">example_key_vault</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">keyvault</span><span class="o">.</span><span class="n">KeyVault</span><span class="p">(</span><span class="s2">&quot;exampleKeyVault&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">tenant_id</span><span class="o">=</span><span class="n">current</span><span class="o">.</span><span class="n">tenant_id</span><span class="p">,</span>
    <span class="n">sku_name</span><span class="o">=</span><span class="s2">&quot;standard&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_key_vault</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceKeyVault</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceKeyVault&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">key_vault_id</span><span class="o">=</span><span class="n">example_key_vault</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID the Azure Key Vault resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service Key Vault. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service Key Vault. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service Key Vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service Key Vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service Key Vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service Key Vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID the Azure Key Vault resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service Key Vault. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service Key Vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service Key Vault. Changing this forces a new resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedServiceKeyVault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of additional properties to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>integration_runtime_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration runtime reference to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID the Azure Key Vault resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Linked Service Key Vault. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of parameters to associate with the Data Factory Linked Service Key Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Linked Service Key Vault. Changing this forces a new resource</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceKeyVault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceKeyVault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceMysql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceMysql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linked Service (connection) between MySQL and Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_mysql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceMysql</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceMysql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Server=test;Port=3306;Database=test;User=test;SSLMode=1;UseSystemTrustStore=0;Password=test&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service MySQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service MySQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceMysql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceMysql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServicePostgresql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linked Service (connection) between PostgreSQL and Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_postgresql</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServicePostgresql</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServicePostgresql&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Host=example;Port=5432;Database=example;UID=example;EncryptionMethod=0;Password=example&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service PostgreSQL. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service PostgreSQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service PostgreSQL. Changing this forces a new resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServicePostgresql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServicePostgresql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">LinkedServiceSqlServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linked Service (connection) between a SQL Server and Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_linked_service_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">LinkedServiceSqlServer</span><span class="p">(</span><span class="s2">&quot;exampleLinkedServiceSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="o">=</span><span class="s2">&quot;Integrated Security=False;Data Source=test;Initial Catalog=test;User ID=test;Password=test&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.additional_properties">
<code class="sig-name descname">additional_properties</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.additional_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of additional properties to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string in which to authenticate with the SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.integration_runtime_name">
<code class="sig-name descname">integration_runtime_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.integration_runtime_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration runtime reference to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Linked Service SQL Server. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Linked Service SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Linked Service SQL Server. Changing this forces a new resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_runtime_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.LinkedServiceSqlServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.LinkedServiceSqlServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Pipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">Pipeline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activities_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Pipeline inside a Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_pipeline</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">(</span><span class="s2">&quot;examplePipeline&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">example_factory</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_resource_group</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">variables</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;bob&quot;</span><span class="p">:</span> <span class="s2">&quot;item1&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">activities_json</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;[</span>
<span class="s2">        {</span>
<span class="s2">                &quot;name&quot;: &quot;Append variable1&quot;,</span>
<span class="s2">                &quot;type&quot;: &quot;AppendVariable&quot;,</span>
<span class="s2">                &quot;dependsOn&quot;: [],</span>
<span class="s2">                &quot;userProperties&quot;: [],</span>
<span class="s2">                &quot;typeProperties&quot;: {</span>
<span class="s2">                        &quot;variableName&quot;: &quot;bob&quot;,</span>
<span class="s2">                        &quot;value&quot;: &quot;something&quot;</span>
<span class="s2">                }</span>
<span class="s2">        }</span>
<span class="s2">]</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activities_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON object that contains the activities that will be associated with the Data Factory Pipeline.</p></li>
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
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.activities_json">
<code class="sig-name descname">activities_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.activities_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON object that contains the activities that will be associated with the Data Factory Pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Data Factory Pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters to associate with the Data Factory Pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.Pipeline.variables">
<code class="sig-name descname">variables</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of variables to associate with the Data Factory Pipeline.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.Pipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activities_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activities_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON object that contains the activities that will be associated with the Data Factory Pipeline.</p></li>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.Pipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.Pipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.TriggerSchedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">TriggerSchedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Trigger Schedule inside a Azure Data Factory.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">example_factory</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Factory</span><span class="p">(</span><span class="s2">&quot;exampleFactory&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_pipeline</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">(</span><span class="s2">&quot;testPipeline&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_resource_group</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
<span class="n">test_trigger_schedule</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">TriggerSchedule</span><span class="p">(</span><span class="s2">&quot;testTriggerSchedule&quot;</span><span class="p">,</span>
    <span class="n">data_factory_name</span><span class="o">=</span><span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_resource_group</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">pipeline_name</span><span class="o">=</span><span class="n">test_pipeline</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">frequency</span><span class="o">=</span><span class="s2">&quot;Day&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Schedule Trigger.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the Schedule Trigger should end. The time will be represented in UTC.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The trigger freqency. Valid values include <code class="docutils literal notranslate"><span class="pre">Minute</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Minute</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval for how often the trigger occurs. This defaults to 1.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>pipeline_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Pipeline name that the trigger will act on.</p></li>
<li><p><strong>pipeline_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The pipeline parameters that the trigger will act upon.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.annotations">
<code class="sig-name descname">annotations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.annotations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags that can be used for describing the Data Factory Schedule Trigger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.data_factory_name">
<code class="sig-name descname">data_factory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.data_factory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.end_time">
<code class="sig-name descname">end_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the Schedule Trigger should end. The time will be represented in UTC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.frequency">
<code class="sig-name descname">frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The trigger freqency. Valid values include <code class="docutils literal notranslate"><span class="pre">Minute</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Minute</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.interval">
<code class="sig-name descname">interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval for how often the trigger occurs. This defaults to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.pipeline_name">
<code class="sig-name descname">pipeline_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.pipeline_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Factory Pipeline name that the trigger will act on.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.pipeline_parameters">
<code class="sig-name descname">pipeline_parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.pipeline_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The pipeline parameters that the trigger will act upon.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datafactory.TriggerSchedule.start_time">
<code class="sig-name descname">start_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.TriggerSchedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">annotations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_factory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TriggerSchedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>annotations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tags that can be used for describing the Data Factory Schedule Trigger.</p></li>
<li><p><strong>data_factory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the Schedule Trigger should end. The time will be represented in UTC.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The trigger freqency. Valid values include <code class="docutils literal notranslate"><span class="pre">Minute</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Minute</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval for how often the trigger occurs. This defaults to 1.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/data-factory/naming-rules">Microsoft documentation</a> for all restrictions.</p>
</p></li>
<li><p><strong>pipeline_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Factory Pipeline name that the trigger will act on.</p></li>
<li><p><strong>pipeline_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The pipeline parameters that the trigger will act upon.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datafactory.TriggerSchedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.TriggerSchedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.TriggerSchedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datafactory.get_factory">
<code class="sig-prename descclassname">pulumi_azure.datafactory.</code><code class="sig-name descname">get_factory</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datafactory.get_factory" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Azure Data Factory (Version 2).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datafactory</span><span class="o">.</span><span class="n">get_factory</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;resource_group_name&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;dataFactoryId&quot;</span><span class="p">,</span> <span class="n">azurerm_data_factory</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Data Factory to retrieve information about.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group where the Data Factory exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
