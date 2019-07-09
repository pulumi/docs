---
---

<div class="section" id="module-pulumi_azure.databricks">
<span id="databricks"></span><h1>databricks<a class="headerlink" href="#module-pulumi_azure.databricks" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.databricks.Workspace">
<em class="property">class </em><code class="descclassname">pulumi_azure.databricks.</code><code class="descname">Workspace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>managed_resource_group_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Databricks Workspace</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>managed_resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">sku</span></code> to use for the Databricks Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code> or <code class="docutils literal notranslate"><span class="pre">premium</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/databricks_workspace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/databricks_workspace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.managed_resource_group_id">
<code class="descname">managed_resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.managed_resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Resource Group created by the Databricks Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.managed_resource_group_name">
<code class="descname">managed_resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.managed_resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">sku</span></code> to use for the Databricks Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code> or <code class="docutils literal notranslate"><span class="pre">premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databricks.Workspace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databricks.Workspace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
