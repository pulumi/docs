---
title: Module costmanagement
title_tag: Module costmanagement | Package pulumi_azure | Python SDK
linktitle: costmanagement
notitle: true
---

<div class="section" id="costmanagement">
<h1>costmanagement<a class="headerlink" href="#costmanagement" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.costmanagement"></span><dl class="class">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.costmanagement.</code><code class="sig-name descname">ResourceGroupExport</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">delivery_info=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">query=None</em>, <em class="sig-param">recurrence_period_end=None</em>, <em class="sig-param">recurrence_period_start=None</em>, <em class="sig-param">recurrence_type=None</em>, <em class="sig-param">resource_group_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Cost Management Export for a Resource Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the cost management export active? Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>delivery_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">delivery_info</span></code> block as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">query</span></code> block as defined below.</p></li>
<li><p><strong>recurrence_period_end</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the export will stop capturing information.</p></li>
<li><p><strong>recurrence_period_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the export will start capturing information.</p></li>
<li><p><strong>recurrence_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often the requested information will be exported. Valid values include <code class="docutils literal notranslate"><span class="pre">Annually</span></code>, <code class="docutils literal notranslate"><span class="pre">Daily</span></code>, <code class="docutils literal notranslate"><span class="pre">Monthly</span></code>, <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the resource group in which to export information.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the container where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolderPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the directory where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage account id where exports will be delivered.</p></li>
</ul>
<p>The <strong>query</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeFrame</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time frame for pulling data for the query. If custom, then a specific time period must be provided. Possible values include: <code class="docutils literal notranslate"><span class="pre">WeekToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">MonthToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">YearToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastWeek</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastYear</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the query.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.active">
<code class="sig-name descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the cost management export active? Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.delivery_info">
<code class="sig-name descname">delivery_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.delivery_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">delivery_info</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the container where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolderPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of the directory where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The storage account id where exports will be delivered.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.query">
<code class="sig-name descname">query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.query" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">query</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeFrame</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time frame for pulling data for the query. If custom, then a specific time period must be provided. Possible values include: <code class="docutils literal notranslate"><span class="pre">WeekToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">MonthToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">YearToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastWeek</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastYear</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the query.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.recurrence_period_end">
<code class="sig-name descname">recurrence_period_end</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.recurrence_period_end" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the export will stop capturing information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.recurrence_period_start">
<code class="sig-name descname">recurrence_period_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.recurrence_period_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the export will start capturing information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.recurrence_type">
<code class="sig-name descname">recurrence_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.recurrence_type" title="Permalink to this definition">¶</a></dt>
<dd><p>How often the requested information will be exported. Valid values include <code class="docutils literal notranslate"><span class="pre">Annually</span></code>, <code class="docutils literal notranslate"><span class="pre">Daily</span></code>, <code class="docutils literal notranslate"><span class="pre">Monthly</span></code>, <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the resource group in which to export information.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">delivery_info=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">query=None</em>, <em class="sig-param">recurrence_period_end=None</em>, <em class="sig-param">recurrence_period_start=None</em>, <em class="sig-param">recurrence_type=None</em>, <em class="sig-param">resource_group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceGroupExport resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the cost management export active? Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>delivery_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">delivery_info</span></code> block as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">query</span></code> block as defined below.</p></li>
<li><p><strong>recurrence_period_end</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the export will stop capturing information.</p></li>
<li><p><strong>recurrence_period_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the export will start capturing information.</p></li>
<li><p><strong>recurrence_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often the requested information will be exported. Valid values include <code class="docutils literal notranslate"><span class="pre">Annually</span></code>, <code class="docutils literal notranslate"><span class="pre">Daily</span></code>, <code class="docutils literal notranslate"><span class="pre">Monthly</span></code>, <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the resource group in which to export information.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the container where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootFolderPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the directory where exports will be uploaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage account id where exports will be delivered.</p></li>
</ul>
<p>The <strong>query</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeFrame</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time frame for pulling data for the query. If custom, then a specific time period must be provided. Possible values include: <code class="docutils literal notranslate"><span class="pre">WeekToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">MonthToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">YearToDate</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastWeek</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">TheLastYear</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the query.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.costmanagement.ResourceGroupExport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.costmanagement.ResourceGroupExport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
